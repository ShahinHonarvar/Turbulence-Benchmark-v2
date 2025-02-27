def all_right_truncatable_prime(n):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = n[35]
    l = [i for i in reversed(range(2, x)) if is_prime(i)]
    r = []
    for i in l:
        t = i
        while t != 0:
            if not is_prime(t):
                break
            t //= 10
        else:
            r.append(i)
    return r