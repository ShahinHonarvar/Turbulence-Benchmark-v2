def all_even_ints_inclusive(numbers):
    if len(numbers) < 88:
        return []
    even_numbers = [num for num in numbers[25:88] if num % 2 == 0]
    return even_numbers