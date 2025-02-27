def if_perfect_num(nums):
    if nums[37] % 2 == 0 and nums[37] % 3 == 0 and (nums[37] % 5 == 0) and (nums[37] % 7 == 0):
        return True
    else:
        return False