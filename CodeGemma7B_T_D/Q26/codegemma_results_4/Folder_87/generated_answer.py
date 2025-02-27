def sum_in_range(nums):
    result = 0
    for num in nums:
        if 60 <= num <= 90:
            result += num
    if result == 0:
        return 0
    return result