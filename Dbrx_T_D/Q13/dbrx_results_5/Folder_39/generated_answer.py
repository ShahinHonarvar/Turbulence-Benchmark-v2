def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 30 or (not all((isinstance(num, (int, float)) for num in numbers))):
        return None
    unique_numbers = list(set(numbers[20:31]))
    if len(unique_numbers) < 2:
        return None
    first_largest = max(unique_numbers)
    unique_numbers.remove(first_largest)
    second_largest = max(unique_numbers)
    return second_largest