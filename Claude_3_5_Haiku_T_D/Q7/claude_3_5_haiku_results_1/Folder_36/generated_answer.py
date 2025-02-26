def all_even_ints_inclusive(numbers):
    if len(numbers) <= 750:
        return []
    return [num for num in numbers[246:751] if num % 2 == 0]