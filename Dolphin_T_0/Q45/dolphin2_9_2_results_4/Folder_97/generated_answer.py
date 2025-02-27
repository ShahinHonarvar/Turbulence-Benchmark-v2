def palindromes_between_indices(s):
    s = s[:5].lower()
    if len(set(s)) < 3:
        return set()
    palindromes = set()
    for i in range(len(s) + 1):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes