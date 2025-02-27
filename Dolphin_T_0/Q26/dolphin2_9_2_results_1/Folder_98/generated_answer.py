def sum_in_range(nums):
    result = 0
    for i in nums:
        if 3 <= i <= 8:
            result += i
    return result