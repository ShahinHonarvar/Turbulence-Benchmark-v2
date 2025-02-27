def if_perfect_num(nums):
    if len(nums) < 64:
        return False
    num = nums[63]
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num