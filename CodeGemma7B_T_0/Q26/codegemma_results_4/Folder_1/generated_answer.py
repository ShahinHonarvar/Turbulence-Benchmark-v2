def sum_in_range(nums):
    sum = 0
    for num in nums:
        if -97 <= num <= -48:
            sum += num
    return sum