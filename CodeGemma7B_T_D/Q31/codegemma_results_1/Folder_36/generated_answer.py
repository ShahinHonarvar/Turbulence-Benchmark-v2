from math import sqrt

def is_perfect_num(nums):
    if nums[990] != int(sqrt(nums[990])) ** 2:
        return False
    return True