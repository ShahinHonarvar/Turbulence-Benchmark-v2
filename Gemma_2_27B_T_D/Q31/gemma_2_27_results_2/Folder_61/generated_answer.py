def if_perfect_num(nums):
    return sum((i for i in range(1, nums[8]) if nums[8] % i == 0)) == nums[8]