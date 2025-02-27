from math import sqrt

def all_left_right_truncatable_prime(n):
    truncatable_primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            left = int(str_num[:i])
            right = int(str_num[i:])
            if not (is_prime(left) and is_prime(right)):
                return False
        return True
    for i in range(n - 1, 0, -1):
        if is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)