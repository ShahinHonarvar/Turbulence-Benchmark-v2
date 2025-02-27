def all_odd_ints_exclusive(int_list):
    if len(int_list) >= 80:
        return [i for i in int_list[64:80] if i % 2 != 0]
    else:
        return []