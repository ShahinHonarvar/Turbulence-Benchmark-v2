def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 50 and num <= 92:
            sum += num
    return sum