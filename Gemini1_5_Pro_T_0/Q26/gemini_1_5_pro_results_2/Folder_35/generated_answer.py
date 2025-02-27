def sum_in_range(nums):
    sum = 0
    for x in nums:
        if x >= 139 and x <= 767:
            sum += x
    return sum