def if_perfect_num(nums):
    if nums[40] % 2 == 0 and nums[40] % 3 == 0 and (nums[40] % 5 == 0):
        return True
    else:
        return False