def if_perfect_num(nums):
    if len(nums) > 849:
        num = nums[849]
        divisors_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisors_sum == num
    return False