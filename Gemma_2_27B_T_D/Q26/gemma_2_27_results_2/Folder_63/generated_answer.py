def sum_in_range(nums):
    sum = 0
    for num in nums:
        if 18 <= num <= 52:
            sum += num
    return sum