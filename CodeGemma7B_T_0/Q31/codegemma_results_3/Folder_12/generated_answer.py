def if_perfect_num(nums):
    if nums[27] % 2 == 0 and nums[27] % 3 == 0 and (nums[27] % 5 == 0) and (nums[27] % 7 == 0):
        return True
    else:
        return False