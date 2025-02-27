def if_perfect_num(nums):
    if nums[56] % 2 == 0 and nums[56] % 3 == 0 and (nums[56] % 5 == 0) and (nums[56] % 7 == 0):
        return True
    else:
        return False