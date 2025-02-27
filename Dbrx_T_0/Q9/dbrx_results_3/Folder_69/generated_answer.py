def all_odd_ints_inclusive(int_list):
    if len(int_list) < 36:
        return []
    odd_ints = [i for i in int_list[32:36] if i % 2 != 0]
    return odd_ints