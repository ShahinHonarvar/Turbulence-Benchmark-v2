def all_odd_ints_inclusive(int_list):
    if len(int_list) < 23:
        return []
    odd_ints = [i for i in int_list[23:] if i % 2 != 0]
    if len(odd_ints) > 0 and len(int_list) > 23:
        odd_ints = [int_list[23]] + odd_ints
    return odd_ints