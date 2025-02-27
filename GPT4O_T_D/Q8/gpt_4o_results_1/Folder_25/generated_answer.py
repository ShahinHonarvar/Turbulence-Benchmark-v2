def all_even_ints_exclusive(numbers):
    if len(numbers) <= 69:
        return []
    return [num for num in numbers[42:69] if num % 2 == 0]