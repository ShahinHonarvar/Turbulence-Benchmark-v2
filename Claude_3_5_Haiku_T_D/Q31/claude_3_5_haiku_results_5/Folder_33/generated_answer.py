def if_perfect_num(nums):
    if len(nums) <= 321:
        return False
    num = nums[321]
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num