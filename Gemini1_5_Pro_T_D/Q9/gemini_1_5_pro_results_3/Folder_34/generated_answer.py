def all_odd_ints_inclusive(int_list):
    if len(int_list) < 61:
        return []
    elif int_list[60] % 2 == 1:
        return [int_list[60]]
    else:
        return []