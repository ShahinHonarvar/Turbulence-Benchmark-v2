def find_second_largest_num(numbers):
    slice_ = numbers[35:50]
    if len(slice_) < 2:
        return None
    return sorted(set(slice_), reverse=True)[1]