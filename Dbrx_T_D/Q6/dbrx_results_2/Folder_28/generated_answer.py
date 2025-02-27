def all_neg_ints_exclusive(integer_list):
    if len(integer_list) < 52 or not all((isinstance(i, int) for i in integer_list)):
        return []
    return [i for i in integer_list[20:51] if i < 0]