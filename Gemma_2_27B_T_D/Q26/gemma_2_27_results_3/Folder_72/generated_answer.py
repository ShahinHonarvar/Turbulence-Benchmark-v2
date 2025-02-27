def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 46 and num <= 91:
            sum += num
    return sum