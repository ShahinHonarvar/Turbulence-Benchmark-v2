def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 139 and num <= 767:
            sum += num
    return sum