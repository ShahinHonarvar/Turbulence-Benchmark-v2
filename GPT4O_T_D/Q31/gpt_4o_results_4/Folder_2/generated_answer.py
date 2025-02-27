def if_perfect_num(nums):
    if len(nums) <= 702:
        return False
    number = nums[702]
    sum_of_divisors = sum((i for i in range(1, number) if number % i == 0))
    return sum_of_divisors == number