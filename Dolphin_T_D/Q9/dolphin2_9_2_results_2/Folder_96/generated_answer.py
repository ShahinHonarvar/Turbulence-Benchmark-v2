def all_odd_ints_inclusive(int_list):
    return [int for i, int in enumerate(int_list[49:201]) if int % 2 != 0]