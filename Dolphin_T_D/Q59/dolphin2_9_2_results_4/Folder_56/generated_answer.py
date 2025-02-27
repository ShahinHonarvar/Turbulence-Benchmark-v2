def all_left_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers_tuple[30]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            left_truncated = i
            while left_truncated > 0:
                if not is_prime(left_truncated):
                    break
                left_truncated //= 10
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)