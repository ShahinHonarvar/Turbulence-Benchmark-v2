def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 8 or (not all((isinstance(num, (int, float)) for num in numbers))):
        return None
    numbers = numbers[5:8]
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1] if sorted_numbers[1] != sorted_numbers[0] else None