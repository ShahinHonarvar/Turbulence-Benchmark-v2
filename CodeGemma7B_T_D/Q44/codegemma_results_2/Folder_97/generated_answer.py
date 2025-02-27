import math

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(15, 40):
        if nums[i] % 2 == 1 and (not is_prime(nums[i])):
            composite_nums.add(nums[i])
    return composite_nums

def is_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True