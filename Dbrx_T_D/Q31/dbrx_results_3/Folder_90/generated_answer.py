def if_perfect_num(nums):
    if len(nums) > 263 and nums[263] == sum([x for x in range(1, nums[263]) if nums[263] % x == 0]):
        return True
    else:
        return False