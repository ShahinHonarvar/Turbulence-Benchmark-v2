def if_perfect_num(nums):
    if nums[993] % 2 == 0 and nums[993] % 3 == 0 and (nums[993] % 5 == 0) and (nums[993] % 7 == 0):
        return True
    else:
        return False