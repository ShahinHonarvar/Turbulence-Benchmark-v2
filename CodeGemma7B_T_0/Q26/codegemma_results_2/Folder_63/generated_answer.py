def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 18 and num <= 52:
            sum += num
    return sum