def find_second_smallest_num(numbers):
    slice = sorted(numbers[10:67])
    if len(slice) < 2:
        return None
    else:
        return slice[1]