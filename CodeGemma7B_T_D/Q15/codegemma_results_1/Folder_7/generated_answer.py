def sum_odd_ints_inclusive(int_list):
    i = 661
    for i in int_list[566:]:
        if i % 2 == 1:
            sum += i
            i += 1
    return sum