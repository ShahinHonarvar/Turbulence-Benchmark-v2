def if_perfect_num(nums):
    return True if nums[132] % sum([i for i in range(1, nums[132]) if nums[132] % i == 0]) == 0 else False