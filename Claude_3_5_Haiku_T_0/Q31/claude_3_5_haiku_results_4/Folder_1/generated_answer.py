def if_perfect_num(nums):
    if len(nums) <= 85:
        return False
    num = nums[85]
    if num <= 1:
        return False
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num