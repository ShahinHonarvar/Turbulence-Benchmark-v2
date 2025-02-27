def find_second_largest_num(numbers):
    slice_numbers = numbers[62:79]
    sorted_numbers = sorted(slice_numbers, reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]