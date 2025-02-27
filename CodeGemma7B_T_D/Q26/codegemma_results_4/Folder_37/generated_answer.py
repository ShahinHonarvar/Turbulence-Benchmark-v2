def sum_in_range(nums):
    sum_nums = 0
    for n in nums:
        if 1 <= n <= 8:
            sum_nums += n
    return sum_nums