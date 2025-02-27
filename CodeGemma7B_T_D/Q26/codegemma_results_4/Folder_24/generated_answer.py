def sum_in_range(nums):
    sum_nums = 0
    for num in nums:
        if -91 <= num <= -41:
            sum_nums += num
    return sum_nums if sum_nums != 0 else 0