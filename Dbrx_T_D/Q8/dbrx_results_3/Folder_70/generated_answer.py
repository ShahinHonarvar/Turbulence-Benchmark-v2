def all_even_ints_exclusive(numbers):
    if not numbers or len(numbers) < 81:
        return []
    return [num for num in numbers[38:81] if num % 2 == 0]