def if_perfect_num(nums):
    if nums[88] % 2 != 0:
        return False
    elif nums[88] % 3 != 0:
        return False
    elif nums[88] % 5 != 0:
        return False
    elif nums[88] % 7 != 0:
        return False
    else:
        return True