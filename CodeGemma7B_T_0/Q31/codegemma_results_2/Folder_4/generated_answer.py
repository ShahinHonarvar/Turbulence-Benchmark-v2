def if_perfect_num(nums):
    if nums[15] % 2 == 0 and nums[15] % 3 == 0 and (nums[15] % 5 == 0) and (nums[15] % 7 == 0):
        return True
    else:
        return False