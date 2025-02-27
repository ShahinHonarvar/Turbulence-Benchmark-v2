def if_perfect_num(nums):
    if nums[23] == sum(range(1, nums[23], 2)):
        return True
    else:
        return False