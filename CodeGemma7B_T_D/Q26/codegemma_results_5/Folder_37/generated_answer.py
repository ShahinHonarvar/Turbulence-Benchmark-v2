def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num in range(1, 9):
            sum += num
    return sum