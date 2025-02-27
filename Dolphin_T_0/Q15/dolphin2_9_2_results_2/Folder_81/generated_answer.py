def sum_odd_ints_inclusive(list_of_ints):
    total_sum = 0
    for i in range(10, 101):
        total_sum += list_of_ints[i]
    return total_sum