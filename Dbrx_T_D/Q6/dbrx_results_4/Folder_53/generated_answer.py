def all_neg_ints_exclusive(integer_list):
    if len(integer_list) < 200:
        raise ValueError('List has fewer than 200 elements')
    return [i for i in integer_list[100:200] if i < 0]