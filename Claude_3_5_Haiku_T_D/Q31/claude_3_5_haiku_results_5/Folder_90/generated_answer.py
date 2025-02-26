def if_perfect_num(nums):
    if len(nums) <= 263:
        return False
    n = nums[263]
    if n <= 0:
        return False
    divisor_sum = sum((i for i in range(1, n) if n % i == 0))
    return divisor_sum == n