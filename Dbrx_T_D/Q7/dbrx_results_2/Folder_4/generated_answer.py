def all_even_ints_inclusive(numbers):
    if len(numbers) < 93:
        return []
    even_numbers = [num for num in numbers[12:93] if num % 2 == 0]
    return even_numbers