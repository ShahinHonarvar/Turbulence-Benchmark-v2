def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 1 and num <= 7:
            sum += num
    return sum