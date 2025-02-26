def if_perfect_num(nums):
    if len(nums) <= 685:
        return False
    n = nums[685]
    divisors_sum = sum((i for i in range(1, n) if n % i == 0))
    return divisors_sum == n