def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(20, 201):
        if i % 2 != 0 and i in nums:
            total += i
    return total