def all_even_ints_inclusive(numbers):
    if len(numbers) < 49:
        return []
    return [num for num in numbers[30:49] if num % 2 == 0]