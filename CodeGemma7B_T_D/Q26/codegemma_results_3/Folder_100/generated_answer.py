def sum_in_range(nums):
    result = 0
    for num in nums:
        if num in range(19, 33):
            result += num
    return result or 0