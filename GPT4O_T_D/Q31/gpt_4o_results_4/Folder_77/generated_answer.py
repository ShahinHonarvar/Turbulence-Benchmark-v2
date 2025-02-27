def if_perfect_num(nums):
    if len(nums) <= 985:
        return False
    n = nums[985]
    if n < 2:
        return False
    sum_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors == n