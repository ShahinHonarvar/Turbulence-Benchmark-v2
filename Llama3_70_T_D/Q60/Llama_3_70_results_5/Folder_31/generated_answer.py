def all_left_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    x = n[50]
    truncatable_primes = [i for i in range(2, x + 1) if '0' not in str(i) and is_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)