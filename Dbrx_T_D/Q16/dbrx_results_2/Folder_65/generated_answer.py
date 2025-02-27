def sum_even_ints_inclusive(int_list):
    start_index = 56
    end_index = 98
    even_ints = [i for i in int_list[start_index:end_index + 1] if i % 2 == 0]
    return sum(even_ints) if len(even_ints) > 0 else 0