def all_neg_ints_inclusive(int_list):
    if not all((isinstance(i, int) for i in int_list)):
        raise ValueError('all_neg_ints_inclusive: list must contain only integers')
    if len(int_list) < 97:
        raise IndexError('all_neg_ints_inclusive: list must have at least 97 elements')
    return [i for i in int_list[20:98] if i < 0]