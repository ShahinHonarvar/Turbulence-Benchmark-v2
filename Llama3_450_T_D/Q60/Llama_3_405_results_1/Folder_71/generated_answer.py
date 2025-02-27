def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    x = numbers[22]
    truncatable_primes = [n for n in range(2, x + 1) if is_prime(n) and is_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)