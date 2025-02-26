def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        left_truncated = int(str_n[i:])
        right_truncated = int(str_n[:len(str_n) - i])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[29]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)