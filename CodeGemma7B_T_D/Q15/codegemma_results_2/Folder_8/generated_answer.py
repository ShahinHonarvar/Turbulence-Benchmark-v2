def sum_odd_ints_inclusive(nums):
    sum = 0
    for num in nums:
        if num >= 23 and num <= 23 and (num % 2 != 0):
            sum += num
    return sum