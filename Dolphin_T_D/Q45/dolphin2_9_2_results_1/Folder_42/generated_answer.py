def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = set(s)
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 2, n + 1):
            if s[i:j] == s[j - 1::-1]:
                palindromes.add(s[i:j])
    return palindromes