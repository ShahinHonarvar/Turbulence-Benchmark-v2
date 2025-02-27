def sum_in_range(nums):
    sum_result = 0
    for num in nums:
        if num >= 4 and num <= 8:
            sum_result += num
    return sum_result