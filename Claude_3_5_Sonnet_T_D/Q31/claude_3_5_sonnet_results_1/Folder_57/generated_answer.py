def if_perfect_num(nums):
    if len(nums) <= 92:
        return False
    num = nums[92]
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num