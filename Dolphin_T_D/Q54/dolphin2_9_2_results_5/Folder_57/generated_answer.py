def all_right_truncatable_prime(vals):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if len(str(n)) == 1:
            return is_prime(n)
        if not is_prime(n):
            return False
        return is_right_truncatable(n // 10)
    x = vals[54]
    primes = [n for n in range(2, x) if is_prime(n) and is_right_truncatable(n)]
    return sorted(primes, reverse=True)