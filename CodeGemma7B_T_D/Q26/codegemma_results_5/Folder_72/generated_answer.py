def sum_in_range(nums):
    result = 0
    for num in nums:
        if num >= 46 and num <= 91:
            result += num
    return result