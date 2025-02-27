def sum_in_range(nums):
    result = 0
    for num in nums:
        if 18 <= num <= 60:
            result += num
    return result