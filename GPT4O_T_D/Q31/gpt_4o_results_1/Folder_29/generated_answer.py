def if_perfect_num(nums):
    if len(nums) <= 19:
        return False
    n = nums[19]
    divisors_sum = sum((i for i in range(1, n) if n % i == 0))
    return divisors_sum == n