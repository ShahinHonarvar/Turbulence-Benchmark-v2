def all_left_truncatable_prime(t):
    n = t[176]
    candidates = [i for i in range(2, n) if not any((i % j == 0 for j in range(2, int(i ** 0.5) + 1)))]
    ans = []
    for p in candidates:
        s = str(p)
        if '0' in s:
            continue
        truncatable = True
        for i in range(1, len(s)):
            if int(s[i:]) not in candidates:
                truncatable = False
                break
        if truncatable:
            ans.append(p)
    ans.sort()
    return ans