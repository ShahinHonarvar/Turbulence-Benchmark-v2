def all_pos_ints_inclusive(int_list):
    pos_ints_list = [x for x in int_list[246:751] if x > 0]
    if not pos_ints_list:
        return []
    else:
        return pos_ints_list