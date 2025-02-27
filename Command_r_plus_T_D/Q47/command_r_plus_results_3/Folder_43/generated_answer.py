def palindromes_of_specific_lengths(s: str) -> set:
    s = s[40:90].lower()
    palindromes = set()
    for length in range(23, 39):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes