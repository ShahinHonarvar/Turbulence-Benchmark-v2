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

def is_left_truncatable_prime(n):
    if n == 0:
        return False
    num = n
    while num != 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_truncatable_prime(nums):
    x = nums[33]
    return sorted([n for n in range(x) if is_left_truncatable_prime(n)])