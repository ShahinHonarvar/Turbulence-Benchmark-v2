def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncated_primes(n):
        if is_prime(n) and '0' not in str(n):
            num = str(n)
            while len(num) > 1:
                num = num[1:]
                if not is_prime(int(num)):
                    return False
                num = num[:-1]
                if not is_prime(int(num)):
                    return False
            return True
        return False
    x = t[26]
    return sorted([i for i in range(2, x + 1) if truncated_primes(i)])