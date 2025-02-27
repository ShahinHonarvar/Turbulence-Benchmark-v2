def all_pos_ints_exclusive(int_list):
    if all((num <= 0 for num in int_list[41:69])):
        return []
    else:
        return [n for n in int_list[41:69] if n > 0]