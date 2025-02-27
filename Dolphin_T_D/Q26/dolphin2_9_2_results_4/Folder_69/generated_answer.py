def sum_in_range(nums):
    result = 0
    for num in nums:
        if 739 <= num <= 928:
            result += num
    return result if result != 0 else 0