def all_odd_ints_inclusive(int_list):
    odd_ints = []
    if len(int_list) > 6:
        if int_list[6] % 2 != 0:
            odd_ints.append(int_list[6])
    return odd_ints