def if_perfect_num(nums):
    if nums[78] % 2 == 0 and nums[78] % 3 == 0 and (nums[78] % 5 == 0) and (nums[78] % 7 == 0):
        return True
    return False