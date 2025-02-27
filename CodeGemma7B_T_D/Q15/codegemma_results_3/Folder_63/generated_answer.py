def sum_odd_ints_inclusive(int_list):
    total = 0
    for i in range(22, 89):
        if i >= 22 and i <= 88 and (int_list[i] % 2 != 0):
            total += int_list[i]
    if total == 0:
        return 0
    return total