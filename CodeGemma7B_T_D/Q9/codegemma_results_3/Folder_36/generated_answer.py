def all_odd_ints_inclusive(num_list):
    if not any((i % 2 != 0 for i in num_list[246:751])):
        return []
    return num_list[246:751][::2]