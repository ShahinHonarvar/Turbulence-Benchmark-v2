def all_odd_ints_exclusive(int_list):
    result = [i for i in int_list[15:99] if i % 2 != 0]
    return result if result else []