def sum_in_range(nums):
    sum_of_nums = 0
    for num in nums:
        if num >= 4 and num <= 7:
            sum_of_nums += num
    return sum_of_nums