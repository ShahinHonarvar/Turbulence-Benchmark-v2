def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= -97 and num <= -48:
            sum += num
    return sum