def if_perfect_num(nums):
    if len(nums) <= 35:
        return False
    num = nums[35]
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num