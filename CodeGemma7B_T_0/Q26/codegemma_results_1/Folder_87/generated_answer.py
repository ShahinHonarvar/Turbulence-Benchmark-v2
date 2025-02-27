def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 60 and num <= 90:
            sum += num
    return sum