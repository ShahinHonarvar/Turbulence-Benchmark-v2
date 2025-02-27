def sum_in_range(nums):
    sum_nums = 0
    for num in nums:
        if 18 <= num <= 60:
            sum_nums += num
    return sum_nums