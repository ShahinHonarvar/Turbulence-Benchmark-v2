def all_even_ints_exclusive(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Argument must be a list')
    if len(numbers) < 200:
        raise IndexError('List must have at least 200 elements')
    even_numbers = [num for num in numbers[20:200] if num % 2 == 0]
    return even_numbers