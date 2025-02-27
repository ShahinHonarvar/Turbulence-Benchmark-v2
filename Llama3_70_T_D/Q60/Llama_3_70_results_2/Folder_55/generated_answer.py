def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    if '0' in str(n):
        return False
    s = str(n)
    if len(s) < 3:
        return is_prime(n)
    for i in range(2, len(s)):
        if not is_prime(int(s[:i])) or not is_prime(int(s[i:])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[73]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return sorted(left_right_truncatable_primes, reverse=True)