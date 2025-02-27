def all_odd_ints_inclusive(int_list):
    if len(int_list) >= 53:
        odd_ints = [i for i in int_list[25:53] if i % 2 != 0]
        return odd_ints
    else:
        return []