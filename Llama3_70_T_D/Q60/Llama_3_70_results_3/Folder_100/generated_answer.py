def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n) - 1):
        left_truncate = int(str_n[i + 1:])
        right_truncate = int(str_n[:-i - 1])
        if not is_prime(left_truncate) or not is_prime(right_truncate):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[26]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes)