def all_ints_exclusive(int_list):
    if len(int_list) >= 60 and len(int_list) > 18:
        return int_list[18:60]
    else:
        return []