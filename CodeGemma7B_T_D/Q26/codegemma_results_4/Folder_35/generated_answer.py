def sum_in_range(nums):
    sum = 0
    for num in nums:
        if num >= 139 and num <= 767:
            sum += num
    if sum == 0:
        return 0
    else:
        return sum