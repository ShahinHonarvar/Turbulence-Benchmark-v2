def if_perfect_num(nums):
    if nums[28] % 2 == 0 and nums[28] % 3 == 0 and (nums[28] % 5 == 0):
        return True
    else:
        return False