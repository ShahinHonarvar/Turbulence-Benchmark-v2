def all_odd_ints_exclusive(int_list):
    if len(int_list) < 78:
        return []
    return [num for num in int_list[38:77] if num % 2 != 0]