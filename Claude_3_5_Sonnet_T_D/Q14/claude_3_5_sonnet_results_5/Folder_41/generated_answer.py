def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    slice = numbers[4:5]
    if len(slice) < 2:
        return None
    sorted_slice = sorted(slice)
    return sorted_slice[1] if len(sorted_slice) > 1 else None