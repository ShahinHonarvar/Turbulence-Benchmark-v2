def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num in range(32, 45):
            sum += num
    return sum