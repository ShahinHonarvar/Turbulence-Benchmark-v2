def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[70]
    truncatable_primes = []
    for n in range(2, x + 1):
        if '0' not in str(n) and is_truncatable(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)

def is_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        left_truncated = int(str_num[i:])
        right_truncated = int(str_num[:-i])
        if not (is_prime(left_truncated) and is_prime(right_truncated)):
            return False
    return True