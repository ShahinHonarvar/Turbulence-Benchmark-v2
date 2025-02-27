def if_perfect_num(nums):
    if len(nums) < 33:
        return False
    number = nums[33]
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum == number