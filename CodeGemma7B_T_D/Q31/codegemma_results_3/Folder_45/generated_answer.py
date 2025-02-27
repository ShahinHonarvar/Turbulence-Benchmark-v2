def if_perfect_num(nums):
    if nums[33] >= 6:
        if nums[33] % 2 == 0:
            if nums[33] / 2 >= 2:
                if nums[33] / 3 >= 2:
                    if nums[33] / 5 >= 2:
                        return True
    return False