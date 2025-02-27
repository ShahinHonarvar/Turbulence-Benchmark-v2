def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[55]
    lr_truncatable_primes = []
    for i in range(10, x + 1):
        if '0' not in str(i) and is_prime(i) and left_right_truncatable(i):
            lr_truncatable_primes.append(i)
    return sorted(lr_truncatable_primes, reverse=True)