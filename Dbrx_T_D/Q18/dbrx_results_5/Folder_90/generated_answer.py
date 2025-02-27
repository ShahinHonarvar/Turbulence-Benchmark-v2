def sum_ints_div_by_either_nums(nums):
    start_index = 138
    end_index = 424
    divisors = [-863, -329]
    total = 0
    for i in range(start_index, end_index + 1):
        for divisor in divisors:
            if nums[i] % divisor == 0:
                total += nums[i]
                break
    return total