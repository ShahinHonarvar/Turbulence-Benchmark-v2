def all_odd_ints_exclusive(int_list):
    odd_range = [int_list[i] for i in range(81, 86) if int_list[i] % 2 != 0]
    return odd_range