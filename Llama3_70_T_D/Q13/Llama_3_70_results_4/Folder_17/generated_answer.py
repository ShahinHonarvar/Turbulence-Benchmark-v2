def find_second_largest_num(numbers):
    slice_numbers = numbers[62:79]
    sorted_numbers = sorted(set(slice_numbers), reverse=True)
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None