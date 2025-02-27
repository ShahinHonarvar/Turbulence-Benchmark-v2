def all_right_truncatable_prime(t):
    x = t[30]
    for f in range(2, x // 2 + 1):
        if x % f == 0:
            return []
    l = []
    for i in range(10 ** (len(str(x)) - 1), x):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            l.append(i)
    l.sort(reverse=True)
    return l