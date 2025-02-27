def if_perfect_num(nums):
    if nums[4] % 2 == 0 and nums[4] % 3 == 0 and (nums[4] % 5 == 0):
        return True
    else:
        return False