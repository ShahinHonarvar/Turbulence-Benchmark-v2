def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        s = 3
        while s * s <= n:
            if n % s == 0:
                return False
            s += 2
        return True

    def is_right_truncatable_prime(n):
        s = str(n)
        r = int(s[-1])
        while r > 0 and s != '2':
            if not is_prime(int(s)):
                return False
            s = str(int(s) // 10)
            r = int(s[-1])
        return True
    x = t[1]
    primes = [i for i in range(0, x) if is_prime(i) and is_right_truncatable_prime(i)]
    return sorted(primes, reverse=True)