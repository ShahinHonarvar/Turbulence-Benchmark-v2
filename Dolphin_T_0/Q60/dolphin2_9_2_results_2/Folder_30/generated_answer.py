def all_left_right_truncatable_prime(arg):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def trunc(n):
        while n > 10:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    primes = [i for i in range(arg[37]) if is_prime(i) and i % 10 != 0]
    primes = [i for i in primes if trunc(i)]
    return sorted(primes, reverse=True)