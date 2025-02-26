def find_second_smallest_num(numbers):
    if len(numbers) <= 41:
        return None
    slice_of_list = numbers[40:201]
    if len(slice_of_list) < 2:
        return None
    sorted_slice = sorted(set(slice_of_list))
    return sorted_slice[1] if len(sorted_slice) >= 2 else None