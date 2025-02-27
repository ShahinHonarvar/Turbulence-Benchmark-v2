def sum_in_range(nums):
    result = 0
    for num in nums:
        if num >= 139 and num <= 767:
            result += num
    return result