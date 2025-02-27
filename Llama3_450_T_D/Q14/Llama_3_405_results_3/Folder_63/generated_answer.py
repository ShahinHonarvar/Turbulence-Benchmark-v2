def find_second_smallest_num(numbers):
    slice_of_numbers = numbers[56:83]
    sorted_numbers = sorted(slice_of_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]