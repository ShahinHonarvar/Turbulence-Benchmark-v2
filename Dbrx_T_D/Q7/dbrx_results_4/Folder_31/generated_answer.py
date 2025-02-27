def all_even_ints_inclusive(numbers):
    if len(numbers) < 89:
        return []
    return [num for num in numbers[75:89] if num % 2 == 0]