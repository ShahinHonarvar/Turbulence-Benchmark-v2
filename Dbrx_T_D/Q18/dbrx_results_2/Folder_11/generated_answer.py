def sum_ints_div_by_either_nums(nums):
    target_divisors = (-85, -30)
    sum = 0
    for i in range(22, 25):
        if i < len(nums) and any((num % divisor == 0 for divisor in target_divisors)):
            sum += nums[i]
    return sum if sum != 0 else 0