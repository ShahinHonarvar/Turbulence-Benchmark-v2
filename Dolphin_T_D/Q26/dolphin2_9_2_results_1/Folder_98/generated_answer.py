def sum_in_range(nums):
    result = 0
    for num in nums:
        if 3 <= num <= 8:
            result += num
    if result == 0:
        return 0
    else:
        return result