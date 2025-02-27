def sum_in_range(nums):
    if not nums:
        return 0
    result = 0
    for num in nums:
        if 13 <= num <= 35:
            result += num
    return result