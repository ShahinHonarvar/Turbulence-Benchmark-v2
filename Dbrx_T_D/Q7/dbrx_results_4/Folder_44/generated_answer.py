def all_even_ints_inclusive(numbers):
    if 13 > len(numbers) or 68 < len(numbers):
        return []
    return [num for num in numbers[13:69] if num % 2 == 0]