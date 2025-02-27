def all_odd_ints_inclusive(int_list):
    if len(int_list) < 61:
        return []
    result = [x for x in int_list[60:61] if x % 2 != 0]
    return result