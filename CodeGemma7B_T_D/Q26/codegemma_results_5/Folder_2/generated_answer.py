def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 266 and num <= 586:
            sum += num
    return sum or 0