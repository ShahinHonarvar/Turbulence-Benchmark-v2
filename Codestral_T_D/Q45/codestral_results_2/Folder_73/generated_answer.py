def palindromes_between_indices(s):
    s = s[3:7].lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 3, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes