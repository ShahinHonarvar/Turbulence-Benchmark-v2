def all_odd_ints_exclusive(ints):
    odd_ints = [int for i, int in enumerate(ints[57:84]) if i != 0 and i != len(ints[57:84]) - 1 and (int % 2 != 0)]
    return odd_ints