def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 36 - 33 + 1:
        return None
    unique_numbers = set(numbers[33:37])
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]