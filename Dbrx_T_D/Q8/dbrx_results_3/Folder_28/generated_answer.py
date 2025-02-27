def all_even_ints_exclusive(numbers):
    if len(numbers) < 52:
        return []
    else:
        return [num for num in numbers[20:52] if num % 2 == 0]