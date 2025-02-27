def find_second_largest_num(numbers):
    slice_ = sorted(numbers[37:52])[::-1]
    if len(slice_) < 2:
        return None
    return slice_[1]