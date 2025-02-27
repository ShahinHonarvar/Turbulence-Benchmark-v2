def find_second_smallest_num(numbers):
    slice_numbers = numbers[5:8]
    if len(slice_numbers) < 2:
        return None
    else:
        return sorted(slice_numbers)[1]