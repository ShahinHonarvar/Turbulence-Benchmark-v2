def all_left_right_truncatable_prime(numbers):
    x = numbers[84]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)