def if_perfect_num(nums):
    if len(nums) <= 56:
        return False
    num = nums[56]
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num