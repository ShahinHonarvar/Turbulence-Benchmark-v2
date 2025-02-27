def find_second_largest_num(lst):
    if len(lst) < 95:
        return None
    else:
        slice_ = lst[75:95]
        sorted_slice = sorted(set(slice_), reverse=True)
        if len(sorted_slice) < 2:
            return None
        else:
            return sorted_slice[1]