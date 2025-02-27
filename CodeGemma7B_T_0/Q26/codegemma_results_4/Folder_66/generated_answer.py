def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 28 and num <= 96:
            sum += num
    return sum