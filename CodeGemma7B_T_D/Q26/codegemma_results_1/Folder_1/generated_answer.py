def sum_in_range(nums):
    result = 0
    for num in nums:
        if num in range(-97, -48 + 1):
            result += num
    return result or 0