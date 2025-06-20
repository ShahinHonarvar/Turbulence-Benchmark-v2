def if_perfect_num(nums):
    if len(nums) <= 926:
        return False
    num = nums[926]
    if num < 2:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num