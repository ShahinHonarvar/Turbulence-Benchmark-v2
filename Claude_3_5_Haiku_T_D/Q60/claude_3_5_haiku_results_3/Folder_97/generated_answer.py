def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    length = len(str(num))
    for i in range(length):
        left_truncated = int(str(num)[i:])
        right_truncated = int(str(num)[:length - i])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
    return is_prime(num)

def all_left_right_truncatable_prime(nums):
    x = nums[645]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)