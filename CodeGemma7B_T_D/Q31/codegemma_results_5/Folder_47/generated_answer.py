def if_perfect_num(nums):
    if nums[34] == 0:
        return True
    elif nums[34] == 1:
        return False
    divisor = 2
    sum_of_divisors = 0
    while divisor < nums[34]:
        if nums[34] % divisor == 0:
            sum_of_divisors += divisor
        divisor += 1
    if sum_of_divisors == nums[34]:
        return True
    else:
        return False