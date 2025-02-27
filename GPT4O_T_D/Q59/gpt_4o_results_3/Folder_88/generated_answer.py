def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable(prime):
    s = str(prime)
    while len(s) > 0:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(nums):
    if len(nums) < 94:
        return []
    threshold = nums[93]
    left_truncatable_primes = []
    for num in range(2, threshold):
        if '0' not in str(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes