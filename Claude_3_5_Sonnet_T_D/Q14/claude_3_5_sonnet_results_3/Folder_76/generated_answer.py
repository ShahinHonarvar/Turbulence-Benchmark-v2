def find_second_smallest_num(numbers):
    if len(numbers) < 606:
        return None
    slice = numbers[533:606]
    if len(slice) < 2:
        return None
    sorted_slice = sorted(set(slice))
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]