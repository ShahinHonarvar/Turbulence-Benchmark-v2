def if_perfect_num(nums):
    if nums[84] % 2 == 0 and nums[84] % 3 == 0 and (nums[84] % 5 == 0):
        return True
    else:
        return False