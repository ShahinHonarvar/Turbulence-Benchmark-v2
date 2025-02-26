def all_even_ints_inclusive(numbers):
    if len(numbers) <= 200:
        return []
    return [num for num in numbers[20:201] if num % 2 == 0]