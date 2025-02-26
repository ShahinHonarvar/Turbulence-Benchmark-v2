def find_second_smallest_num(numbers):
    slice = numbers[262:747]
    if len(slice) < 2:
        return None
    sorted_slice = sorted(set(slice))
    return sorted_slice[1] if len(sorted_slice) >= 2 else None