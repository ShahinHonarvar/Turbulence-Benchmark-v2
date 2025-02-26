def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    for i in range(1, len(s)):
        left = int(s[i:])
        right = int(s[:len(s) - i])
        if not is_prime(left) or not is_prime(right):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(nums):
    x = nums[14]
    result = []
    for num in range(x, 11, -1):
        if is_truncatable_prime(num):
            result.append(num)
    return result