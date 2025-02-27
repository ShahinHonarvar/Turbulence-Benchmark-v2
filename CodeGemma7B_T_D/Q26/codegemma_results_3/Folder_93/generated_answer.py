def sum_in_range(nums):
    sum_of_nums = 0
    for num in nums:
        if num >= -23 and num <= 64:
            sum_of_nums += num
    return sum_of_nums