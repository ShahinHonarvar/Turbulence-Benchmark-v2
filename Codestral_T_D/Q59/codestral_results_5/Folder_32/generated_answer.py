def all_left_truncatable_prime(numbers):
    x = numbers[42]
    trunc_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for num in range(2, x):
        if is_truncatable_prime(num):
            trunc_primes.append(num)
    return sorted(trunc_primes)