def all_even_ints_exclusive(numbers):
    if len(numbers) <= 2:
        return []
    return [num for num in numbers[1:-1] if num % 2 == 0]