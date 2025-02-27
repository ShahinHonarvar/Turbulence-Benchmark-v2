def palindromes_of_specific_lengths(s):
    s = s[:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for length in range(4, 6):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes