def all_pos_ints_inclusive(lst):
    result = [num for num in lst[209:557] if num > 0]
    if result:
        return result
    else:
        return []