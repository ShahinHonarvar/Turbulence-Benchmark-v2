def sum_odd_ints_inclusive(nums):
    sum = 0
    for num in nums[32:36]:
        if num % 2 == 1:
            sum += num
    return sum or 0