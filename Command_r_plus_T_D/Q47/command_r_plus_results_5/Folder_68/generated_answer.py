def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    s = s.lower()
    for i in range(51):
        for j in range(i + 50, min(i + 101, len(s))):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes