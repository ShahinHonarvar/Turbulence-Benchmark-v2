def all_right_truncatable_prime(n):
    if len(n) < 3:
        return []
    x = n[3]
    res = []
    for i in range(x // 10 ** 6 + 1):
        n = str(i + 1)
        if n[-1] == '9':
            n = int(n[:-1])
        if all((n % d == 0 for d in range(2, int(n ** 0.5) + 1))):
            break
        res.append(int(n))
    return res