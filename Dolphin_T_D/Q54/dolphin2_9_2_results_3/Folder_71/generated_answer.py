def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n == 1:
            return False
        for c in str(n):
            if not is_prime(int(n)):
                return False
            n = int(n[:-1])
        return True
    x = t[22]
    r = []
    for i in range(1, x):
        if is_right_truncatable(i):
            r.append(i)
    return sorted(r, reverse=True)