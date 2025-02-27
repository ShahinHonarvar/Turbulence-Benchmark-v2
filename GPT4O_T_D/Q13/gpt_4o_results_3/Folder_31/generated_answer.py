def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    subset = numbers[75:89]
    unique_numbers = set(subset)
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers)[-2]