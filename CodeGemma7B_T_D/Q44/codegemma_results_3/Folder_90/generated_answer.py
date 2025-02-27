from math import sqrt

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(333, 368 + 1):
        if i in nums:
            if not is_prime(i):
                composite_nums.add(i)
    return composite_nums

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