def find_second_largest_num(lst):
    slice_ = sorted(lst[533:606], reverse=True)
    return slice_[1] if len(slice_) > 1 else None