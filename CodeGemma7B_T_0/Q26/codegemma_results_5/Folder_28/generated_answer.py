def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 10 and num <= 97:
            sum += num
    return sum