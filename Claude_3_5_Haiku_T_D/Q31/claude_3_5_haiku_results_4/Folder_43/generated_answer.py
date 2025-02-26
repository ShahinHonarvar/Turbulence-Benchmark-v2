def if_perfect_num(nums):
    if len(nums) <= 29:
        return False
    num = nums[29]
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num