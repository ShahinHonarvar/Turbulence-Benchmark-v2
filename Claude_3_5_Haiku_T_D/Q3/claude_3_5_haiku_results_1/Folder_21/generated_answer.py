def all_pos_ints_inclusive(integers):
    if len(integers) <= 975:
        return []
    result = [num for num in integers[639:976] if num > 0]
    return result