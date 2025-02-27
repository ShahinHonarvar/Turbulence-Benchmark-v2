def sum_in_range(nums):
    result = 0
    for num in nums:
        if -3 <= num <= 6:
            result += num
    return result