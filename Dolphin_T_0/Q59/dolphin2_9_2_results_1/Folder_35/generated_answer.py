def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n < 2:
            return False
        for i in range(len(str(n)) - 1, 0, -1):
            if str(n)[i] == '0':
                return False
            m = int(str(n)[i:])
            if not is_prime(m):
                return False
        return True
    x = t[177]
    left_truncatable_primes = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    return sorted(left_truncatable_primes)