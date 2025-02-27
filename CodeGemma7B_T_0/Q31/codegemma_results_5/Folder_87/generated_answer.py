def if_perfect_num(nums):
    if nums[96] % 2 == 0 and nums[96] % 3 == 0 and (nums[96] % 5 == 0) and (nums[96] % 7 == 0):
        return True
    else:
        return False