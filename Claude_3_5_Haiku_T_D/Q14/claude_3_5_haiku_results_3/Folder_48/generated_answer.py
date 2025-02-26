def find_second_smallest_num(numbers):
    if len(numbers) < 248:
        return None
    slice_list = numbers[246:751]
    if len(slice_list) < 2:
        return None
    try:
        sorted_slice = sorted(set(slice_list))
        return sorted_slice[1] if len(sorted_slice) >= 2 else None
    except:
        return None