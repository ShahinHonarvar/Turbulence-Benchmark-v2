def sum_in_range(nums):
    sum_result = 0
    for num in nums:
        if num >= 1 and num <= 7:
            sum_result += num
    return sum_result