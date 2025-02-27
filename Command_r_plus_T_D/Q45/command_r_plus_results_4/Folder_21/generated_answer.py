def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(1, min(8, len(s)) + 1):
        for j in range(i + 6, min(i + 7, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes