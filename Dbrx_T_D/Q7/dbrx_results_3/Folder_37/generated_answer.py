def all_even_ints_inclusive(numbers):
    if len(numbers) < 6:
        return []
    return [num for num in numbers[1:6] if num % 2 == 0]