def if_perfect_num(nums):
    if nums[33] % 2 == 0 and nums[33] % 3 == 0 and (nums[33] % 5 == 0) and (nums[33] % 7 == 0):
        return True
    else:
        return False