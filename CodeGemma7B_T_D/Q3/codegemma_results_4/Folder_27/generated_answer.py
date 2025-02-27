def all_pos_ints_inclusive(pos_ints):
    if not pos_ints:
        return []
    elif pos_ints[66] <= 0 and pos_ints[93] <= 0:
        return []
    else:
        return pos_ints[66:94]