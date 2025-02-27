def sum_even_ints_inclusive(int_list):
    even_ints = [i for i in int_list[62:100] if i % 2 == 0]
    return sum(even_ints) if len(even_ints) > 0 else 0