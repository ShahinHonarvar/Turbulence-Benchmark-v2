def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 4 and num <= 6:
            sum += num
    return sum