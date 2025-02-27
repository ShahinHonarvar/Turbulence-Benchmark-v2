def sum_in_range(nums):
    result = 0
    for num in nums:
        if -10 <= num <= 48:
            result += num
    return result