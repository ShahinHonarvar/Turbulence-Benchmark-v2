def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 93 or len(numbers) > 10000:
        return None
    numbers_in_range = numbers[18:93]
    unique_numbers = list(set(numbers_in_range))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if unique_numbers[0] != unique_numbers[1] else None