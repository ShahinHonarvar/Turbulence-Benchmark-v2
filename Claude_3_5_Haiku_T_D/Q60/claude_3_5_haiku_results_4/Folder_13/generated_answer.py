def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    s = str(num)
    if '0' in s:
        return False
    for i in range(len(s)):
        left_trunc = int(s[i:])
        right_trunc = int(s[:len(s) - i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[784]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes