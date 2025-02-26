def all_even_ints_exclusive(numbers):
    if len(numbers) < 11:
        return []
    even_numbers = [num for num in numbers[9:11] if num % 2 == 0]
    return even_numbers