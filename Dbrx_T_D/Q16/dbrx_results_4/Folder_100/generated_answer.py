def sum_even_ints_inclusive(int_list):
    start_index = 42
    end_index = 68
    return sum((x for x in int_list[start_index:end_index + 1] if x % 2 == 0))