def all_even_ints_inclusive(numbers):
    if len(numbers) < 15:
        return []
    else:
        return [num for num in numbers[7:15] if num % 2 == 0]