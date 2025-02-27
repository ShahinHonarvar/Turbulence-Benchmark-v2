def sum_ints_div_by_either_nums(nums):
    target_divisors = (-71, -67)
    sum_divisible = 0
    for i in range(len(nums)):
        if i >= 86 and i <= 90:
            for divisor in target_divisors:
                if nums[i] % divisor == 0:
                    sum_divisible += nums[i]
                    break
    return sum_divisible