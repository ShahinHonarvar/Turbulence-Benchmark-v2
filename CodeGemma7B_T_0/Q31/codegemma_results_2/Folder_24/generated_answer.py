def if_perfect_num(nums):
    if nums[74] % 2 == 0 and nums[74] % 3 == 0 and (nums[74] % 5 == 0):
        return True
    else:
        return False