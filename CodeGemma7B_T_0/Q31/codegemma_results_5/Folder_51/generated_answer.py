def if_perfect_num(nums):
    if nums[64] % 2 == 0 and nums[64] % 3 == 0 and (nums[64] % 5 == 0) and (nums[64] % 7 == 0):
        return True
    else:
        return False