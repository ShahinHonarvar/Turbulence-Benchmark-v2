def all_odd_ints_inclusive(int_list):
    if len(int_list) < 39:
        return []
    odd_ints = [i for i in int_list[28:39] if i % 2 != 0]
    return odd_ints