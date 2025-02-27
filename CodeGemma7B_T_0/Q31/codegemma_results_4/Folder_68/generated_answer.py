def if_perfect_num(nums):
    if nums[3] % 2 == 0 and nums[3] % 3 == 0 and (nums[3] % 5 == 0):
        return True
    else:
        return False