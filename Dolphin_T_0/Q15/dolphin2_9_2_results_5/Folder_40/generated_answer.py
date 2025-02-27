def sum_odd_ints_inclusive(ints):
    ints_in_range = ints[0:3]
    odd_sum = 0
    for int in ints_in_range:
        if int % 2 != 0:
            odd_sum += int
    return odd_sum