def all_even_ints_exclusive(numbers):
    if len(numbers) < 9:
        return []
    return [num for num in numbers[2:8] if num % 2 == 0]