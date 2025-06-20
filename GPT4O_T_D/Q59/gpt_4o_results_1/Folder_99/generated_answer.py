def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(s):
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(nums):
    if len(nums) <= 758:
        return []
    x = nums[758]
    result = []
    for n in range(2, x):
        if '0' not in str(n) and is_left_truncatable(str(n)):
            result.append(n)
    return sorted(result)