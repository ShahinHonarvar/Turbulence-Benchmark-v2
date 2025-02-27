def all_odd_ints_exclusive(integer_list):
    if len(integer_list) < 2:
        return []
    return [i for i in integer_list[0:2] if i % 2 != 0]