def find_subset_of_length_n(s):
    if not s:
        return 0
    n = len(s)
    if n < 860:
        return 0
    ans = 1
    for i in range(860, n + 1):
        p = 1
        for j in range(i):
            p *= n - j
        ans *= p
        for j in range(1, i + 1):
            ans //= j
    return ans