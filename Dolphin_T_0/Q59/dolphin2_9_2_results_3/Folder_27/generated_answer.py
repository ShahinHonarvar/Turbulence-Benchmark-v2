def all_left_truncatable_prime(x):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        for digit in str(n):
            digit = int(digit)
            if digit == 0:
                return False
            n = int(str(n)[1:])
        return is_prime(n)
    primes = [n for n in range(10, x) if is_prime(n) and is_left_truncatable(n)]
    return sorted(primes, reverse=True)