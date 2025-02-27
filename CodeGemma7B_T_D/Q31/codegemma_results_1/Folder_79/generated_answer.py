def if_perfect_num(nums):
    total = sum(nums[:63])
    return total == nums[63]