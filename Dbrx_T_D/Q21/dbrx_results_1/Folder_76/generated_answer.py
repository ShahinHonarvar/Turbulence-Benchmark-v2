def all_ints_div_by_num(lst):
    if not all((isinstance(i, int) for i in lst)):
        raise ValueError('All elements in the list must be integers')
    return [i for i in lst[601:699] if i % 901 == 0]