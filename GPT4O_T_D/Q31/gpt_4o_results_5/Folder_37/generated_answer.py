def if_perfect_num(nums):
    if len(nums) <= 28:
        return False
    num = nums[28]
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num