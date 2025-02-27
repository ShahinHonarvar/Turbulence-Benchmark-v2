def if_perfect_num(nums):
    if nums[21] % 2 == 0 and nums[21] % 3 == 0 and (nums[21] % 5 == 0):
        return True
    else:
        return False