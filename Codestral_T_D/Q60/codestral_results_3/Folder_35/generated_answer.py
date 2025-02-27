def all_left_right_truncatable_prime(t):
    x = t[177]

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
        num_str = str(n)
        for i in range(1, len(num_str)):
            left_truncated = int(num_str[i:])
            right_truncated = int(num_str[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)