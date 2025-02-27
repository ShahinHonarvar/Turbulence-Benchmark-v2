def palindromes_between_indices(s):
    s = s[1:6]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 2, n + 1):
            substr = s[i:j]
            if substr == substr[::-1] and len(substr) >= 6:
                palindromes.add(substr)
    return palindromes