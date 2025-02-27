def all_left_right_truncatable_prime(numbers):
    x = numbers[32]

    def is_prime(n):
        if n <= 1:
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
            if n == 0:
                break
        n = str(numbers[32])
        while n > 0:
            if not is_prime(int(n)):
                return False
            n = n[1:]
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)