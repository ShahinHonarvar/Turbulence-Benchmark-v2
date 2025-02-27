def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return True
    x = numbers[14]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    primes_truncatable = [i for i in primes if is_truncatable(i)]
    return sorted(primes_truncatable, reverse=True)