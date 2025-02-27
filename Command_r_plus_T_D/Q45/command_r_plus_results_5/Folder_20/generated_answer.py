def palindromes_between_indices(s: str) -> set:
    s = s[2:9].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes