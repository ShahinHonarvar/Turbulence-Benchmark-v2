def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    s = str(num)
    while len(s) > 1:
        s = s[1:-1]
        if s and (not is_prime(int(s))):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    if len(nums) <= 93:
        return []
    x = nums[93]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes