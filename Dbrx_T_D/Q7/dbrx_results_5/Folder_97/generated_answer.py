def all_even_ints_inclusive(numbers):
    if len(numbers) < 80:
        return []
    return [n for n in numbers[40:81] if n % 2 == 0]