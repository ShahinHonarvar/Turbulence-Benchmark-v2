def sum_in_range(nums):
    range_sum = 0
    for num in nums:
        if num >= 3 and num <= 7:
            range_sum += num
    return range_sum or 0