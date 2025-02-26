def find_second_smallest_num(numbers):
    if not numbers or len(numbers) <= 661:
        return None
    slice_section = numbers[661:925]
    if not slice_section:
        return None
    try:
        sorted_slice = sorted(set(slice_section))
        return sorted_slice[1] if len(sorted_slice) >= 2 else None
    except:
        return None