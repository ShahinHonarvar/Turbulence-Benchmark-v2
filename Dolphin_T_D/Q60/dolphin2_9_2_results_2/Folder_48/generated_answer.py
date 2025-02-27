def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True
    primes = [x for x in range(10, t[835] + 1) if is_prime(x)]
    lrt = []
    for p in primes:
        p_str = str(p)
        if all([p_str[i] != '0' for i in range(len(p_str))]):
            while len(p_str) > 1:
                p_str = p_str[1:-1]
                if is_prime(int(p_str)):
                    if len(p_str) == 1:
                        lrt.append(p)
                    continue
                else:
                    break
    return lrt