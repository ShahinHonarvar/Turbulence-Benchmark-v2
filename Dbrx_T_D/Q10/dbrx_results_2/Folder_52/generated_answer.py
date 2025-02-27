def all_odd_ints_exclusive(int_list):
    slice = int_list[93:94]
    odd_ints = [i for i in slice if i % 2 != 0]
    return odd_ints