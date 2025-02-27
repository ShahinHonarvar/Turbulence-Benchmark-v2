def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[18]
    right_truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            truncated_num = n
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    break
                truncated_num = truncated_num // 10
            if truncated_num == 0:
                right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes, reverse=True)