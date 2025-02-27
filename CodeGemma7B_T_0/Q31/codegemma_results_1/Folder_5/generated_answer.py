def if_perfect_num(nums):
    if nums[67] % 2 == 0 and nums[67] % 3 == 0 and (nums[67] % 5 == 0) and (nums[67] % 7 == 0):
        return True
    else:
        return False