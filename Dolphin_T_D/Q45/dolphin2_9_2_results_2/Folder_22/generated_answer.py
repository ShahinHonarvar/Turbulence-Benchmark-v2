def palindromes_between_indices(s):
    letter_set = set(s[5:7].lower())
    palindromes = set()
    for length in range(3, len(s)):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length].lower()
            if all((char in letter_set for char in substr)):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes