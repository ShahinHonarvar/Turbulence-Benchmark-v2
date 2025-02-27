def if_perfect_num(nums):
    if nums[38] ** 2 == sum((n ** 2 for n in range(1, nums[38] + 1))):
        return True
    return False