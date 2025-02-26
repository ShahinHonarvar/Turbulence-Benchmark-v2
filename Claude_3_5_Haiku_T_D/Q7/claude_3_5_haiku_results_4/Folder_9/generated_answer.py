def all_even_ints_inclusive(numbers):
    if len(numbers) < 74:
        return []
    current_number = numbers[73]
    return [current_number] if current_number % 2 == 0 else []