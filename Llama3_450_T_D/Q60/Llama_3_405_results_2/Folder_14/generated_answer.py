def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i] or num_str)
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                return False
        return True
    x = t[78]
    truncatable_primes = [i for i in range(11, x + 1) if is_prime(i) and is_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)