def if_perfect_num(nums):
    if nums[57] % 2 == 0 and nums[57] % 3 == 0 and (nums[57] % 5 == 0) and (nums[57] % 7 == 0):
        return True
    else:
        return False