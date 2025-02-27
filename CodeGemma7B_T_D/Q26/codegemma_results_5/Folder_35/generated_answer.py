def sum_in_range(nums):
    """Sum of all elements in the range [139,767]"""
    result = 0
    for num in nums:
        if num in range(139, 768):
            result += num
    return result