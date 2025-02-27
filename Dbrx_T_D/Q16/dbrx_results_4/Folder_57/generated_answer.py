def sum_even_ints_inclusive(int_list):
    if not isinstance(int_list, list) or not all((isinstance(i, int) for i in int_list)):
        raise ValueError('Input should be a list of integers')
    if len(int_list) < 55:
        return 0
    return sum((x for x in int_list[27:56] if x % 2 == 0))