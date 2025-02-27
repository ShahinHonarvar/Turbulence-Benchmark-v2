def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[4]
    return sorted([n for n in range(10, x + 1) if is_left_right_truncatable_prime(n)])