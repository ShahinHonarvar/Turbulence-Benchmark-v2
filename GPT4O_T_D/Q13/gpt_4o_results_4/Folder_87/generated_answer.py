def find_second_largest_num(numbers):
    if len(numbers) < 47:
        return None
    segment = numbers[36:47]
    if len(segment) < 2:
        return None
    unique_numbers = set(segment)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]