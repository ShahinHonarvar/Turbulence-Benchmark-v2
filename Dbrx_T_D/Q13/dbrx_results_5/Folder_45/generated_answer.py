def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 250 or (not isinstance(numbers, list)):
        return None
    unique_numbers = set(numbers[30:201])
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None