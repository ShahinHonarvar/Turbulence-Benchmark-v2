def if_perfect_num(nums):
    if nums[845] % 2 == 0 and nums[845] % 3 == 0 and (nums[845] % 5 == 0) and (nums[845] % 7 == 0):
        return True
    else:
        return False