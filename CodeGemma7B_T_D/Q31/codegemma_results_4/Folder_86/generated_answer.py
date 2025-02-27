def if_perfect_num(nums):
    return 284 + nums[194] == sum([i for i in range(1, sum(nums[:194]) + nums[194] + 1) if nums[194] % i == 0])