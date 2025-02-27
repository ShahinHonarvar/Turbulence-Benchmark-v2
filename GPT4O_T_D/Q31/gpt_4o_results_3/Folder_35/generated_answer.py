def if_perfect_num(nums):
    if len(nums) <= 993:
        return False
    num = nums[993]
    if num <= 1:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num