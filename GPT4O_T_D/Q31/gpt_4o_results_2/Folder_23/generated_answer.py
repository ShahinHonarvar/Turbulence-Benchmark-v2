def if_perfect_num(nums):
    if len(nums) <= 69:
        return False
    n = nums[69]
    sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors == n