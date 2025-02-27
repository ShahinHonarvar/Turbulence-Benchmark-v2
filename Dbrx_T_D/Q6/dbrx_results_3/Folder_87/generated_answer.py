def all_neg_ints_exclusive(int_list):
    if not all((isinstance(i, int) for i in int_list)):
        raise ValueError('all_neg_ints_exclusive: List must contain only integers')
    if len(int_list) < 99:
        return []
    return [i for i in int_list[32:99] if i < 0]