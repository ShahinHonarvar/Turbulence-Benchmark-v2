def sum_in_range(nums):
    sum = 0
    for num in nums:
        if 2 <= num <= 7:
            sum += num
    return sum