def if_perfect_num(nums):
    if len(nums) <= 33:
        return False
    num = nums[33]
    if num < 2:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num