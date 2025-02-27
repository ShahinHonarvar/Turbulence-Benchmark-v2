def all_even_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    even_numbers = [num for num in numbers[80:201] if num % 2 == 0]
    return even_numbers