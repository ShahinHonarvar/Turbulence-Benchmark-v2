def sum_even_ints_inclusive(int_list):
    even_ints = [i for i in int_list[3:6] if i % 2 == 0]
    return sum(even_ints) if even_ints else 0