def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 42 or len(numbers) > 68:
        return None
    first_smallest = min(numbers[42:68])
    first_smallest_index = numbers[42:68].index(first_smallest) + 42
    filtered_numbers = [n for n in numbers if n > first_smallest]
    if not filtered_numbers:
        return None
    second_smallest = min(filtered_numbers)
    second_smallest_index = numbers.index(second_smallest)
    return second_smallest if second_smallest_index >= 42 and second_smallest_index <= 68 else None