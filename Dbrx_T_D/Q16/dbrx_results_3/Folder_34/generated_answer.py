def sum_even_ints_inclusive(int_list):
    if len(int_list) < 200:
        return 'Input list should have at least 200 elements.'
    else:
        even_ints = [i for i in int_list[60:201] if i % 2 == 0]
        return sum(even_ints) if even_ints else 0