def all_odd_ints_inclusive(int_list):
    if not any((i % 2 for i in int_list[8:10])):
        return []
    return [i for i in int_list[8:10] if i % 2]