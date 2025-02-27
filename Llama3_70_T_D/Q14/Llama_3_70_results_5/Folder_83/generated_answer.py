def find_second_smallest_num(lst):
    slice = sorted(lst[90:201])
    return slice[1] if len(slice) > 1 else None