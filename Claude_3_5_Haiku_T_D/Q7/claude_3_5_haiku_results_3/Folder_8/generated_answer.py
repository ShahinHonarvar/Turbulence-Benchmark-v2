def all_even_ints_inclusive(numbers):
    if len(numbers) <= 23:
        return []
    target_number = numbers[23]
    return [num for num in numbers[23:24] if num % 2 == 0]