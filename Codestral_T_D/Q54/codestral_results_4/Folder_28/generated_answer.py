def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[19]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            right_truncated_num = num
            is_right_truncatable = True
            while right_truncated_num > 0:
                right_truncated_num //= 10
                if not is_prime(right_truncated_num):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)