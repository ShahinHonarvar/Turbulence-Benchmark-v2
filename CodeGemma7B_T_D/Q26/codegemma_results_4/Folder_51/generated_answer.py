def sum_in_range(nums):
    result = 0
    for num in nums:
        if num >= 2 and num <= 7:
            result += num
    return result