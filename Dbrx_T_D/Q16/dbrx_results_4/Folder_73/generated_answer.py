def sum_even_ints_inclusive(int_list):
    selected_ints = int_list[19:93]
    even_ints = [i for i in selected_ints if i % 2 == 0]
    return sum(even_ints) if even_ints else 0