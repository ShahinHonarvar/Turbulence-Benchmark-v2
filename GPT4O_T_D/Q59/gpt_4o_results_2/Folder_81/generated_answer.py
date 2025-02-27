def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if '0' in str(num):
        return False
    if not is_prime(num):
        return False
    num_str = str(num)
    while len(num_str) > 1:
        num_str = num_str[1:]
        if not is_prime(int(num_str)):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[98]
    left_truncatable_primes = []
    for i in range(2, x):
        if left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes