def all_even_ints_inclusive(numbers):
    if len(numbers) < 95:
        return []
    even_numbers = [num for num in numbers[75:95] if num % 2 == 0]
    return even_numbers