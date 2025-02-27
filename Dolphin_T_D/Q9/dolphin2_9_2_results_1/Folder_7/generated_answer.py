def all_odd_ints_inclusive(int_list):
    odd_ints = [i for i in int_list[661:925] if i % 2 != 0]
    if odd_ints:
        return odd_ints
    else:
        return []