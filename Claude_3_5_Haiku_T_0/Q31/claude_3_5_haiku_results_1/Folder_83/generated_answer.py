def if_perfect_num(nums):
    if len(nums) <= 95:
        return False
    num = nums[95]
    if num <= 1:
        return False
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num