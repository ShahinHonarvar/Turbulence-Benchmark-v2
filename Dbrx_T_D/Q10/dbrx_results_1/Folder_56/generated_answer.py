def all_odd_ints_exclusive(int_list):
    if len(int_list) < 9:
        return []
    odd_ints = [i for i in int_list[7:9] if i % 2 != 0]
    return odd_ints