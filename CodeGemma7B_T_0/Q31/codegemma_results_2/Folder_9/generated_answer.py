def if_perfect_num(nums):
    if nums[24] % 2 == 0 and nums[24] % 3 == 0 and (nums[24] % 5 == 0) and (nums[24] % 7 == 0):
        return True
    return False