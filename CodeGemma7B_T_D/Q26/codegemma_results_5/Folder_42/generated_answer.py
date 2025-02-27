def sum_in_range(nums):
    result = 0
    for num in nums:
        if 141 <= num <= 262:
            result += num
    return result if result else 0