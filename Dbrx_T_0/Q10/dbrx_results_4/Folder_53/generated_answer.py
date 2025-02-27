def all_odd_ints_exclusive(int_list):
    if len(int_list) < 102:
        return []
    else:
        return [i for i in int_list[100:101] if i % 2 != 0]