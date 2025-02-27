def gcf_three_nums(nums):
    a = nums[17]
    b = nums[88]
    c = nums[35]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    actual_gcf = a
    while actual_gcf != c:
        if actual_gcf > c:
            actual_gcf -= c
        else:
            c -= actual_gcf
    return actual_gcf