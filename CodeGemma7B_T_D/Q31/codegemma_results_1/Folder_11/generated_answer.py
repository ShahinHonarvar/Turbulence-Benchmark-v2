def if_perfect_num(nums):
    return nums[77] == sum((i for i in range(1, nums[77]) if nums[77] % i == 0))