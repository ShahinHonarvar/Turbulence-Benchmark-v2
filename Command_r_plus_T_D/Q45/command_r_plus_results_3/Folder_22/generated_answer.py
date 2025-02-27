def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(5, len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes