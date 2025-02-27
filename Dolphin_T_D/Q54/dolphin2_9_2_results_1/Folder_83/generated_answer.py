def all_right_truncatable_prime(num_tuple):

    def check_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def check_right_truncatable(n):
        while n > 1:
            n = n // 10
            if not check_prime(n):
                return False
        return True
    x = num_tuple[24]
    primes = [i for i in range(2, x) if check_prime(i) and check_right_truncatable(i)]
    return sorted(primes)