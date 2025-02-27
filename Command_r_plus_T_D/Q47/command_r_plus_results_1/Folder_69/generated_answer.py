def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(11, 97):
        for j in range(i + 44, min(i + 52, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes