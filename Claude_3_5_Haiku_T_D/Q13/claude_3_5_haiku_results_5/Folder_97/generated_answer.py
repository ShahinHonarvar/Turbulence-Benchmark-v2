def find_second_largest_num(numbers):
    if len(numbers) <= 40:
        return None
    slice_section = numbers[40:81]
    if len(slice_section) <= 1:
        return None
    sorted_section = sorted(slice_section, reverse=True)
    return sorted_section[1]