def if_perfect_num(nums):
    if len(nums) <= 851:
        return False
    num = nums[851]
    if num <= 1:
        return False
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num