def all_left_right_truncatable_prime(numbers):
    x = numbers[792]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            left_truncated = n[i:]
            right_truncated = n[:-i] if i != 0 else n
            if not (is_prime(int(left_truncated)) and is_prime(int(right_truncated))):
                return False
        return True
    truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable_prime(i)]
    return truncatable_primes