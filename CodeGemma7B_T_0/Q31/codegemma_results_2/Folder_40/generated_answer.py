def if_perfect_num(nums):
    if nums[7] % 2 == 0 and nums[7] % 3 == 0 and (nums[7] % 5 == 0) and (nums[7] % 7 == 0):
        return True
    else:
        return False