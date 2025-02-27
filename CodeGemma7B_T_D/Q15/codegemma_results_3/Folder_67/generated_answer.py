def sum_odd_ints_inclusive(list_of_ints):
    total_sum = 0
    for i in range(22, 51):
        if list_of_ints[i] % 2 != 0:
            total_sum += list_of_ints[i]
    return total_sum