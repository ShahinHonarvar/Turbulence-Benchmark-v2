def sum_in_range(nums):
    sum, filtered_nums = (0, [num for num in nums if -616 <= num <= -205])
    for num in filtered_nums:
        sum += num
    return sum