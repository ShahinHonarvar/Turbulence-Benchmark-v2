def sum_in_range(nums):
    result = 0
    for num in nums:
        if num >= 31 and num <= 50:
            result += num
    return result