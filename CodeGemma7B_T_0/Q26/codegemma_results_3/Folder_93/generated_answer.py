def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= -23 and num <= 64:
            sum += num
    return sum