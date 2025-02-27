def all_even_ints_inclusive(int_list):
    even_range = int_list[3:6]
    return [i for i in even_range if i % 2 == 0]