def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[3:301]
    s = s.lower()
    palindromes = set()
    for length in range(30, 301):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes