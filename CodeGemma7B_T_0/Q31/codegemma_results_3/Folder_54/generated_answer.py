def if_perfect_num(nums):
    if nums[51] % 2 == 0 and nums[51] % 3 == 0 and (nums[51] % 5 == 0) and (nums[51] % 7 == 0):
        return True
    else:
        return False