def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    segment = numbers[22:89]
    if len(segment) < 2:
        return None
    unique_numbers = set(segment)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]