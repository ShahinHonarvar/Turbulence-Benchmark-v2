def gcf_three_nums(a):
    num_a = a[25]
    num_b = a[76]
    num_c = a[57]
    while num_a != num_b:
        if num_a > num_b:
            num_a = num_a - num_b
        else:
            num_b = num_b - num_a
    while num_a != num_c:
        if num_a > num_c:
            num_a = num_a - num_c
        else:
            num_c = num_c - num_a
    return num_a