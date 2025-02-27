def gcf_two_nums(nums):
    a = nums[68]
    b = nums[40]
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        greater = a
        smaller = b
    else:
        greater = b
        smaller = a
    factor = greater % smaller
    while factor != 0:
        greater = smaller
        smaller = factor
        factor = greater % smaller
    return smaller