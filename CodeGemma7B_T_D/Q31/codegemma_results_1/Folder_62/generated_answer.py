def if_perfect_num(nums):
    return nums[926] % sum((i for i in range(2, int(nums[926] ** 0.5) + 1) if nums[926] % i == 0)) == 0