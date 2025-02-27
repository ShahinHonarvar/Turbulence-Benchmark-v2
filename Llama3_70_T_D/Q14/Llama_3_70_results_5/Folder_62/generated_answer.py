def find_second_smallest_num(numbers):
    slice_numbers = numbers[10:67]
    sorted_numbers = sorted(slice_numbers)
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    else:
        return None