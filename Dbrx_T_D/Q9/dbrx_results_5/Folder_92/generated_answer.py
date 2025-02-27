def all_odd_ints_inclusive(integer_list):
    if len(integer_list) < 2:
        return []
    odd_ints = [i for i in integer_list[:2] if i % 2 != 0]
    return odd_ints