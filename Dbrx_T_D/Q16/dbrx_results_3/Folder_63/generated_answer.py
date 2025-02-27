def sum_even_ints_inclusive(int_list):
    if len(int_list) < 88:
        return 'Input list should have at least 88 elements'
    else:
        even_ints = [i for i in int_list[21:89] if i % 2 == 0]
        if even_ints:
            return sum(even_ints)
        else:
            return 0