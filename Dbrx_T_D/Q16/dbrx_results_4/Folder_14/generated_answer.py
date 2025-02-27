def sum_even_ints_inclusive(integer_list):
    selected_ints = integer_list[5:8]
    return sum((x for x in selected_ints if x % 2 == 0))