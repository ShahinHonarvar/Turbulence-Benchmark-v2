def if_perfect_num(nums):
    return nums[40] % sum([j for j in range(1, nums[40]) if nums[40] % j == 0]) == 0