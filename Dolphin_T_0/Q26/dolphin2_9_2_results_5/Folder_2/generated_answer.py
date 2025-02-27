def sum_in_range(nums):
    sum = 0
    for num in nums:
        if 266 <= num <= 586:
            sum += num
    if sum == 0:
        return 0
    return sum