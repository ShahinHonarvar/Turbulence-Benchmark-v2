def if_perfect_num(nums):
    if len(nums) <= 162:
        return False
    num = nums[162]
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num