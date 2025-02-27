def all_right_truncatable_prime(t):

    def is_prime(n):
        not_prime = [False] * 2 + [True] * (n // 2 - 1)
        i = 3
        w = 2
        while i * i <= n:
            if not_prime[i]:
                v = w * w
                for u in range(i * i, n + 1, v):
                    not_prime[u] = False
            i += 2
            w += 1
        return not_prime[n]
    x = t[10]
    prime_list = [i for i in range(x - 1, 0, -1) if is_prime(i)]
    right_truncatable = []
    for p in prime_list:
        if all([is_prime(int(p[i:])) for i in range(len(str(p)) - 1)]) and set(str(p)) != {5}:
            right_truncatable.append(p)
    return sorted(right_truncatable, reverse=True)