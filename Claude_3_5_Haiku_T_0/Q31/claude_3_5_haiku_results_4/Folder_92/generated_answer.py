def if_perfect_num(nums):
    if not nums or nums[0] <= 0:
        return False
    num = nums[0]
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num