def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s.lower()
    palindromes = set()
    for length in range(21, 33):
        for start in range(32, 72 - length):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes