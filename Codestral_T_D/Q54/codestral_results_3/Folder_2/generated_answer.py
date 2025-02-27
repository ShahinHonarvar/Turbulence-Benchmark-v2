def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[618]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated = num
            while truncated > 0:
                truncated //= 10
                if not is_prime(truncated):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)