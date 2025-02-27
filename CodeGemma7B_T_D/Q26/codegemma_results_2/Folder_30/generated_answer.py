def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num in range(86, 91):
            sum += num
    return sum or 0