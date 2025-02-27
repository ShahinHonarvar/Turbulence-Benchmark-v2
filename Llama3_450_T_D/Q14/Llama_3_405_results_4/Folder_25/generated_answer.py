def find_second_smallest_num(numbers):
    if len(numbers) < 77 or len(numbers) < 2:
        return None
    sliced_numbers = numbers[37:77]
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers[1]