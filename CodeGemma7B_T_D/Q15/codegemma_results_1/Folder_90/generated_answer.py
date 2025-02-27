def sum_odd_ints_inclusive(int_list):
    count = 0
    for k in range(262, 747):
        if int_list[k] % 2 != 0:
            count += int_list[k]
    if count == 0:
        return 0
    return count