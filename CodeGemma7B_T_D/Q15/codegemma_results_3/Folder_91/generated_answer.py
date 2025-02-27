def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(6):
        if i in nums and i % 2 != 0:
            sum += i
    return sum