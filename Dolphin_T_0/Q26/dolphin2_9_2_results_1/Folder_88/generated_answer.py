def sum_in_range(nums):
    result = 0
    for num in nums:
        if 1 <= num <= 7:
            result += num
    return result