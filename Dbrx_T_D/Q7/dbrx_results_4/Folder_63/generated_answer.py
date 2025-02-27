def all_even_ints_inclusive(numbers):
    if len(numbers) < 88 or 22 > len(numbers):
        return []
    return [num for num in numbers[22:89] if num % 2 == 0]