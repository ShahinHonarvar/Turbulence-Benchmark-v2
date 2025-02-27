def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    slice_ = sorted(numbers[42:69])
    if len(slice_) < 2:
        return None
    return slice_[1]