def find_second_smallest_num(numbers):
    slice = numbers[56:83]
    if len(slice) < 2:
        return None
    sorted_slice = sorted(slice)
    return sorted_slice[1]