def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            left_truncated = int(str(n)[i:])
            right_truncated = int(str(n)[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    x = t[74]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes