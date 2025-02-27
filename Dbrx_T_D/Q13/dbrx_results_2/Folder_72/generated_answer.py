def find_second_largest_num(numbers):
    numbers_slice = numbers[29:52]
    unique_numbers = list(set(numbers_slice))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if unique_numbers[0] != unique_numbers[1] else None