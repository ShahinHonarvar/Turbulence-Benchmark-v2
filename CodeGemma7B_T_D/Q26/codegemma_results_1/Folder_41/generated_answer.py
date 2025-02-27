def sum_in_range(nums):
    result = 0
    for num in nums:
        if 2 <= num <= 4:
            result += num
    return result