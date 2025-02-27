def sum_in_range(nums):
    sum = 0
    for num in nums:
        if 138 <= num <= 858:
            sum += num
    if sum == 0:
        sum = 0
    return sum