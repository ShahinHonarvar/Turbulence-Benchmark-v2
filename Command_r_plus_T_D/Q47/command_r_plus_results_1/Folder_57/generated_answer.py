def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[15:95].lower()
    palindromes = set()
    for length in range(39, 53):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes