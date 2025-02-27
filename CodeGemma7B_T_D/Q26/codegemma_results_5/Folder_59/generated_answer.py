def sum_in_range(nums):
    sum = 0
    for num in nums:
        if 2 <= num <= 3:
            sum += num
    return sum if sum else 0