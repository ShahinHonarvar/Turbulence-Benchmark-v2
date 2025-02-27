def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num in range(7, 10):
            sum += num
    return sum if sum else 0