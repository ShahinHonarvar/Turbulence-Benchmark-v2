def if_perfect_num(nums):
    if len(nums) <= 16:
        return False
    number = nums[16]
    divisors_sum = sum((i for i in range(1, number) if number % i == 0))
    return divisors_sum == number