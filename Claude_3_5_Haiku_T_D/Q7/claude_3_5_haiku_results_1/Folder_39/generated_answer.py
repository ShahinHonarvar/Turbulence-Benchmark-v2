def all_even_ints_inclusive(numbers):
    if len(numbers) <= 30:
        return []
    selected_numbers = numbers[20:31]
    return [num for num in selected_numbers if num % 2 == 0]