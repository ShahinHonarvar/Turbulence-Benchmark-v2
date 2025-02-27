def sum_in_range(nums):
    if not nums:
        return 0
    sum_total = 0
    for num in nums:
        if num >= 46 and num <= 91:
            sum_total += num
    return sum_total