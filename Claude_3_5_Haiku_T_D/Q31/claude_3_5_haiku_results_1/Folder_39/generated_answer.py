def if_perfect_num(nums):
    if len(nums) <= 59:
        return False
    num = nums[59]
    if num <= 0:
        return False
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num