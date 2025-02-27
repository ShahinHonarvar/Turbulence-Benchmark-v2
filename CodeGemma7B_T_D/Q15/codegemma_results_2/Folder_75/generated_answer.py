def sum_odd_ints_inclusive(nums):
    L = 56
    R = 57
    sum = 0
    for i, x in enumerate(nums):
        if i < L or i > R:
            continue
        if x % 2 == 1:
            sum += x
    if not sum:
        return 0
    return sum