def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(527, 539):
        if i in nums and i % 2 != 0:
            total += i
    return total