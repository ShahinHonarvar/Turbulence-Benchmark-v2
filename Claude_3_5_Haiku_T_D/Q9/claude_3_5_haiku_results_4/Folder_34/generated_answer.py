def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 60:
        return []
    selected_number = numbers[60]
    return [selected_number] if selected_number % 2 != 0 else []