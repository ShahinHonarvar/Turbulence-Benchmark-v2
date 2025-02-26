def all_even_ints_inclusive(numbers):
    if len(numbers) <= 88:
        return []
    even_slice = [num for num in numbers[75:89] if num % 2 == 0]
    return even_slice