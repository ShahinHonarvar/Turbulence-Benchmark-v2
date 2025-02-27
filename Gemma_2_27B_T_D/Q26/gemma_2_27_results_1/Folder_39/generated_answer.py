def sum_in_range(nums):
    sum = 0
    for num in nums:
        if 10 <= num <= 79:
            sum += num
    return sum