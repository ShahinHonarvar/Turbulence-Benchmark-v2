def sum_ints_div_by_either_nums(nums):
    divisors = {-74, -58}
    total = 0
    for i in range(10, 80):
        if i >= len(nums):
            break
        if any((num % divisor == 0 for num in (nums[i], nums[i] + 1) for divisor in divisors)):
            total += nums[i]
    return total