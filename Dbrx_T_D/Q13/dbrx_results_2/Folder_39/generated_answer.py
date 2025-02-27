def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 31:
        return None
    numbers = numbers[20:31]
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if unique_numbers[1] != unique_numbers[0] else None