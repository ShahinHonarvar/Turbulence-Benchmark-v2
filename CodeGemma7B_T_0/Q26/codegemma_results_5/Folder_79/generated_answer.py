def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 2 and num <= 9:
            sum += num
    return sum