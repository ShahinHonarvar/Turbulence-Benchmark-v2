def palindrome_of_length_at_least_n(s):
    s = s.lower() + '#'
    n = len(s)
    L = [0] * n
    C = R = 0
    maxR = 0
    res = set()
    for i in range(1, n):
        if i <= maxR:
            L[i] = min(R - i + 1, L[2 * C - i])
        while i - L[i] > 1 and i + L[i] < n and (s[i - L[i] - 1] == s[i + L[i] + 1]):
            L[i] += 1
        if L[i] + i - 1 > maxR:
            C, R = (i, i + L[i] - 1)
            maxR = L[i] + i - 1
        if L[i] >= 17 and s[i - L[i] - 1:i + L[i] + 1] in s:
            res.add(s[i - L[i] - 1:i + L[i] + 1])
    return res