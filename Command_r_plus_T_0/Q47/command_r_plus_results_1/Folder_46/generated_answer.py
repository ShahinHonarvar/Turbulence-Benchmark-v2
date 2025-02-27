def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s.lower()
    palindromes = set()
    for length in range(29, 63):
        for start in range(11, 98 - length):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes