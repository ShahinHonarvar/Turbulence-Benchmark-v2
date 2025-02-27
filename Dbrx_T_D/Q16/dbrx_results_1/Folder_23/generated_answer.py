def sum_even_ints_inclusive(int_list):
    start_index = 52
    end_index = 71
    even_ints = [i for i in int_list[start_index:end_index + 1] if i % 2 == 0]
    return sum(even_ints) if even_ints else 0