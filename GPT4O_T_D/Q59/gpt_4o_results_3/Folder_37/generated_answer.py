def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        truncated = int(str_n[i:])
        if not is_prime(truncated):
            return False
    return True

def all_left_truncatable_prime(nums):
    if len(nums) <= 35:
        return []
    x = nums[35]
    result = []
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)