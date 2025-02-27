def if_perfect_num(nums):
    return nums[845] == sum((i for i in range(1, nums[845]) if nums[845] % i == 0))