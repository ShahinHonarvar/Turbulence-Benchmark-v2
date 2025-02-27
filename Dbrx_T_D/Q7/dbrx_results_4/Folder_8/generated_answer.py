def all_even_ints_inclusive(input_list):
    if len(input_list) < 23:
        return []
    else:
        return [i for i in input_list[23:] if i % 2 == 0][23:]