def if_perfect_num(nums):
    if len(nums) <= 453:
        return False
    number = nums[453]
    divisors_sum = sum((i for i in range(1, number) if number % i == 0))
    return divisors_sum == number