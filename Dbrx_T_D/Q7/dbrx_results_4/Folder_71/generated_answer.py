def all_even_ints_inclusive(numbers):
    if len(numbers) < 52 or len(numbers) < 26:
        return []
    even_numbers = [num for num in numbers[26:53] if num % 2 == 0]
    return even_numbers