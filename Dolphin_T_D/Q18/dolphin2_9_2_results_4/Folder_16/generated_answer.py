def sum_ints_div_by_either_nums(list_of_ints):
    total_sum = 0
    for i in range(55, 81):
        if list_of_ints[i] % 22 == 0 or list_of_ints[i] % 32 == 0:
            total_sum += list_of_ints[i]
    return total_sum if total_sum != 0 else 0