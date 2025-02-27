def sum_odd_ints_inclusive(int_list):
    total = 0
    for i in range(246, 751):
        if i % 2 != 0:
            total += int_list[i]
    return total or 0