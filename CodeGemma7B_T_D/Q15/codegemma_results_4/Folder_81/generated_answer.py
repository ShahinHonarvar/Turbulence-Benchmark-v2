def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(10, 101):
        if i % 2 != 0 and i in nums:
            total += i
    return total or 0