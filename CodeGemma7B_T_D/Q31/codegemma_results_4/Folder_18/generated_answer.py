def if_perfect_num(nums):
    if nums[312] % 2 == 0 and nums[312] ** (1 / 2) - int(nums[312] ** (1 / 2)) == 0:
        return True
    return False