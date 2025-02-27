def all_right_truncatable_prime(args):
    x = args[88]

    def get_prime(num):
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def get_right_truncatable_primes(num):
        primes = []
        while num > 0:
            if get_prime(num):
                primes.append(num)
            num //= 10
        return primes
    right_truncatable_primes = []
    for i in range(1, x):
        primes = get_right_truncatable_primes(i)
        if primes and primes[-1] == i:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)