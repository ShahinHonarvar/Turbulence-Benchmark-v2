def sum_in_range(nums):
    result = 0
    for num in nums:
        if 19 <= num <= 32:
            result += num
    return result or 0