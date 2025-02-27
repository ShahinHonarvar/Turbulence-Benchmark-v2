def all_even_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    even_numbers = [num for num in numbers[90:200] if num % 2 == 0]
    return even_numbers