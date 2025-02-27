def find_second_smallest_num(numbers):
    if len(numbers) < 78:
        return None
    slice_numbers = numbers[66:78]
    sorted_numbers = sorted(slice_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]