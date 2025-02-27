def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        original = n
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return is_prime(original)
    x = numbers[88] if len(numbers) > 88 else 0
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes)