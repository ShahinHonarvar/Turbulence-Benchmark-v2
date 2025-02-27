def all_even_ints_inclusive(numbers):
    if len(numbers) > 7:
        return [num for num in numbers[7:8] if num % 2 == 0]
    return []