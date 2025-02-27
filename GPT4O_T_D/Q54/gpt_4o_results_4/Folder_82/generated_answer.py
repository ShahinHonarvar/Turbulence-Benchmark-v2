def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        return all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)) + 1)))
    x = numbers[69] if len(numbers) > 69 else 0
    rtl_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(rtl_primes, reverse=True)