def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 100 or (not all((isinstance(num, (int, float)) for num in numbers))):
        return None
    unique_numbers = set(numbers[10:101])
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1] if sorted_numbers[1] != sorted_numbers[0] else None