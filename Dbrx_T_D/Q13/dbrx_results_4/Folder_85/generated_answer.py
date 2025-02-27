def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers) < 6:
        return None
    numbers_to_consider = numbers[6:9]
    unique_numbers = set(numbers_to_consider)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]