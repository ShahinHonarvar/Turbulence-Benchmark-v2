def all_even_ints_inclusive(numbers):
    if len(numbers) < 31:
        return []
    return [num for num in numbers[20:31] if num % 2 == 0]