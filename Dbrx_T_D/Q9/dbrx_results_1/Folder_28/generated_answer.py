def all_odd_ints_inclusive(int_list):
    if len(int_list) >= 64 and isinstance(int_list[61], int) and isinstance(int_list[62], int):
        odd_ints = [i for i in int_list[62:63] if i % 2 != 0]
        return odd_ints
    else:
        return []