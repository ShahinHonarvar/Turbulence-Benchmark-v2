def sum_even_ints_inclusive(int_list):
    if not isinstance(int_list, list) or len(int_list) < 86:
        return 0
    return sum((i for i in int_list[75:86] if i % 2 == 0))