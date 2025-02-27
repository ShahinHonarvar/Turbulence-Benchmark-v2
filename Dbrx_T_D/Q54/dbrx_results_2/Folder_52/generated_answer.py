def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = 10 ** (len(str(numbers[52])) - 1)
    primes = []
    for i in range(x, numbers[52]):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)