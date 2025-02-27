def sum_even_ints_inclusive(numeric_list):
    return_sum = 0
    for item in numeric_list[75:86]:
        if item % 2 == 0:
            return_sum += item
    return return_sum