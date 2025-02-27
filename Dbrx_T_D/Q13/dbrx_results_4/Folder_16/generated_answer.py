def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers) - 1 < 36 - 33:
        return None
    numbers = numbers[33:37]
    unique_numbers = list(set(numbers))
    sorted_numbers = sorted(unique_numbers)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[-2]