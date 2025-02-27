def palindromes_of_specific_lengths(s):
    """Return set of palindromes within a specific range and length."""
    di = {}
    for i in range(27, 96):
        for j in range(i + 1, min(len(s), i + 32)):
            for k in range(i + 1, j):
                if s[i] == s[j] == s[k] and s[j] >= 'a' and (s[j] <= 'z'):
                    di[i, j, k] = s[i:j + 1]
    return set(di.values())