def if_perfect_num(nums):
    if nums[88] < 2:
        return False
    sum_divisors = sum((i for i in range(1, nums[88]) if nums[88] % i == 0))
    return sum_divisors == nums[88]