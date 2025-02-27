def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    sliced_numbers = numbers[37:52]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = sorted(set(sliced_numbers))
    return unique_numbers[1] if len(unique_numbers) > 1 else None