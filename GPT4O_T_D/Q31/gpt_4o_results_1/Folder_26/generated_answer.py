def if_perfect_num(nums):
    if len(nums) <= 222:
        return False
    number = nums[222]
    if number < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            sum_of_divisors += i
            if i != number // i:
                sum_of_divisors += number // i
    return sum_of_divisors == number