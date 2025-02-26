def find_second_largest_num(numbers):
    if len(numbers) <= 4:
        return None
    slice_section = numbers[4:5]
    if not slice_section:
        return None
    return slice_section[0]