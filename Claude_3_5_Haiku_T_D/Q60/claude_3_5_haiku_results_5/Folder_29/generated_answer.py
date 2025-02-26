def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        left = int(s[i:])
        right = int(s[:len(s) - i])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[55]
    result = []
    for num in range(x, 11, -1):
        if '0' not in str(num) and is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return result