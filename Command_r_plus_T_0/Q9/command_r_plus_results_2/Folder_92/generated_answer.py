def all_odd_ints_inclusive(int_list):
    odd_ints = [int for int in int_list[:2] if int % 2 != 0]
    return odd_ints