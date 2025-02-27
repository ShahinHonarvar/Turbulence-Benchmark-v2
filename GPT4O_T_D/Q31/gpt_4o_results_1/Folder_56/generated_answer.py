def if_perfect_num(nums):
    if len(nums) <= 60:
        return False
    num = nums[60]
    if num <= 0:
        return False
    sum_divisors = sum((i for i in range(1, num // 2 + 1) if num % i == 0))
    return sum_divisors == num