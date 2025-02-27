def if_perfect_num(nums):
    if nums[537] % 2 == 0 and nums[537] ** 0.5 + 1 % int(nums[537] ** 0.5 + 1) == 1:
        return True
    return False