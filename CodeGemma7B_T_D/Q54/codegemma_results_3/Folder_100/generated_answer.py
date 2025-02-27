def all_right_truncatable_prime(a):
    x = a[26]
    a = a[:26]

    def is_prime(n):
        n = abs(n)
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(p):
        p = str(p)
        for i in range(len(p) - 1):
            p = p[:-1]
            if not is_prime(int(p)):
                return False
        return True
    b = []
    for i in a:
        if is_prime(i) and right_truncatable(i):
            b.append(i)
    b.sort()
    return b if b else []