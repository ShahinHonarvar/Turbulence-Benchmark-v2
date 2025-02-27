def all_odd_ints_inclusive(int_list):
    if len(int_list) < 5:
        return []
    elif int_list[4] % 2 == 0:
        return []
    else:
        return [int_list[4]]