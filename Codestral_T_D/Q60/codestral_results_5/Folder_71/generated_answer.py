def all_left_right_truncatable_prime(t):
    x = t[22]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def truncate(n):
        s = str(n)
        return [int(s[:i]) for i in range(1, len(s))] + [int(s[i:]) for i in range(1, len(s))]
    lrtp = []
    for i in range(2, x + 1):
        if all((is_prime(t) for t in truncate(i))):
            lrtp.append(i)
    return sorted(lrtp, reverse=True)