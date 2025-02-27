def sum_in_range(nums):
    sum_total = 0
    for num in nums:
        if num >= 18 and num <= 52:
            sum_total += num
    if sum_total == 0:
        return 0
    return sum_total