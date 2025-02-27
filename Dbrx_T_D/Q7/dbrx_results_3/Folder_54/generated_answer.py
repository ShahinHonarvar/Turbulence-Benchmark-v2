def all_even_ints_inclusive(numbers):
    if not isinstance(numbers, list):
        raise TypeError('numbers must be a list')
    if not all((isinstance(i, int) for i in numbers)):
        raise TypeError('All elements in numbers must be integers')
    if len(numbers) < 55:
        return []
    return [n for n in numbers[34:56] if n % 2 == 0]