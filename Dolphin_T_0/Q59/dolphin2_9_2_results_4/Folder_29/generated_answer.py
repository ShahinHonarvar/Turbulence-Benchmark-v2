def all_left_truncatable_prime(t):

    def is_left_truncatable(n):
        if n < 10:
            return primer[u]
        return is_left_truncatable(n // 10) and primer[n]

    def is_prime(n):
        if n == 1:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if not n % x:
                return False
        return True
    primer = [False, False] + [True for _ in range(2, 100000)]
    for u in range(2, int(len(primer) ** 0.5) + 1):
        if primer[u]:
            for x in range(u ** 2, len(primer), u):
                primer[x] = False
    x = t[55]
    L = [x for x in range(100000, 0, -1) if is_left_truncatable(x) and is_prime(x)]
    return L[:x]