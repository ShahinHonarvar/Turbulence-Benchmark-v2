def if_perfect_num(nums):
    if nums[60] % 6 == 0:
        return True
    elif nums[60] % 3 == 0:
        return True
    elif nums[60] % 2 == 0:
        return True
    else:
        return False