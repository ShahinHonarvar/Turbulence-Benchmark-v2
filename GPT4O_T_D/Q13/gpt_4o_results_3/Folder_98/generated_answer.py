def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    slice_numbers = numbers[:7]
    unique_numbers = set(slice_numbers)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]