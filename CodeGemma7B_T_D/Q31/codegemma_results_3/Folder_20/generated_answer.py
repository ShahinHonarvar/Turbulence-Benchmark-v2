def if_perfect_num(nums):
    if nums[53] % 2 == 0:
        if nums[53] % 3 == 0:
            if nums[53] % 5 == 0:
                return True
        else:
            return False
    else:
        return False