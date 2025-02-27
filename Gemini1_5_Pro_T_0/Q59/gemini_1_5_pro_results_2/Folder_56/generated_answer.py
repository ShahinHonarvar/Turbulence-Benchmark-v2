def all_left_truncatable_prime(numbers):
    x = numbers[30]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10 and is_prime(n):
            return True
        if '0' in str(n) or not is_prime(n):
            return False
        return is_left_truncatable_prime(int(str(n)[1:]))
    left_truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes