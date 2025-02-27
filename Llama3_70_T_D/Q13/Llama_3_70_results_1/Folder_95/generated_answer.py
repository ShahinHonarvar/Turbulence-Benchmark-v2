def find_second_largest_num(lst):
    if 86 < len(lst):
        slice_ = lst[82:87]
        if len(slice_) > 1:
            return sorted(set(slice_), reverse=True)[1]
        else:
            return None
    else:
        return None