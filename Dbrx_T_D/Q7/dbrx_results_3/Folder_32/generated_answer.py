def all_even_ints_inclusive(numbers):
    if 21 > len(numbers) or 97 < len(numbers):
        return []
    return [num for num in numbers[21:98] if num % 2 == 0]