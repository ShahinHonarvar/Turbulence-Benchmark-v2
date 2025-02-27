def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 38 and num <= 81:
            sum += num
    return sum