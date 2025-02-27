def all_odd_ints_exclusive(int_list):
    if len(int_list) < 99:
        return []
    else:
        odd_ints = [i for i in int_list[43:99] if i % 2 != 0]
        return odd_ints