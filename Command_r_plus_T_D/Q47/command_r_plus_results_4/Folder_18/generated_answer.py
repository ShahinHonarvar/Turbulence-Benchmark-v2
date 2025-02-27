def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[10:84]
    palindromes = set()
    for length in range(13, 67):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes