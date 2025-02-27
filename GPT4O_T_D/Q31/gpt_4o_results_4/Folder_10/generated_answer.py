def if_perfect_num(nums):
    if len(nums) <= 54:
        return False
    number = nums[54]
    if number < 2:
        return False
    divisors_sum = sum((i for i in range(1, number) if number % i == 0))
    return divisors_sum == number