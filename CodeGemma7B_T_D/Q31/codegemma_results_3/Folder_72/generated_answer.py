def if_perfect_num(nums):
    if nums[16] % 2 == 0:
        return True
    elif nums[16] % 3 == 0:
        return True
    elif nums[16] % 5 == 0:
        return True
    elif nums[16] % 7 == 0:
        return True
    else:
        return False