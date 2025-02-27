def all_even_ints_inclusive(numbers):
    if len(numbers) < 93:
        return []
    else:
        return [num for num in numbers[11:93] if num % 2 == 0]