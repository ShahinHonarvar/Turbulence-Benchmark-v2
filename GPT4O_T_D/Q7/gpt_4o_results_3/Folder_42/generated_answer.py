def all_even_ints_inclusive(numbers):
    if len(numbers) < 30:
        return []
    return [number for number in numbers[29:80] if number % 2 == 0]