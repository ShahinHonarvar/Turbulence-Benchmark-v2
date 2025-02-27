def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable_prime(n):
        length = len(str(n))
        for i in range(1, length):
            truncated_n = int(str(n)[i:])
            if not is_prime(truncated_n):
                return False
        return True
    x = numbers[67]
    left_right_truncatable_primes = []
    for n in range(2, x + 1):
        if is_left_truncatable_prime(n) and is_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes, reverse=True)