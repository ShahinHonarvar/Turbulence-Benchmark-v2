def find_second_smallest_num(numbers):
    slice_numbers = numbers[10:101]
    if len(slice_numbers) < 2:
        return None
    else:
        return sorted(slice_numbers)[1]