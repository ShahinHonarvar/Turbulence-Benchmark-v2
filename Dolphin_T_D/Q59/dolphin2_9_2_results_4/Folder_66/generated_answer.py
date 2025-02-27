def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for divisor in range(3, sqrt_n, 2):
            if n % divisor == 0:
                return False
        return True

    def is_truncatable_prime(n):
        num = n
        while num > 0:
            if not is_prime(num):
                return False
            num = num // 10
        if is_prime(n):
            return True
        return False
    x = tup[25]
    left_truncatable_primes = [x for x in range(2, x) if is_truncatable_prime(x)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes