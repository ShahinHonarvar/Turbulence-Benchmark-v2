def if_perfect_num(nums):
    if nums[312] % 2 == 0 and nums[312] % 3 == 0 and (nums[312] % 5 == 0) and (nums[312] % 7 == 0):
        return True
    else:
        return False