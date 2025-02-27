def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncatable(n):
        digits = len(str(n))
        for i in range(1, digits):
            if not is_prime(n % 10 ** i):
                return False
        return True
    x = numbers[70]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)