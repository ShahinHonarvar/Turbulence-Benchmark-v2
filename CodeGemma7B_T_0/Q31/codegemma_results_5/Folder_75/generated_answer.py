def if_perfect_num(nums):
    if nums[80] % 2 == 0 and nums[80] % 3 == 0 and (nums[80] % 5 == 0) and (nums[80] % 7 == 0):
        return True
    else:
        return False