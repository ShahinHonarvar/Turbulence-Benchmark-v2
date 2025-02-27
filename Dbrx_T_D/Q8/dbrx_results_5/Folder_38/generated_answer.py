def all_even_ints_exclusive(numbers):
    if len(numbers) < 41:
        return []
    else:
        return [num for num in numbers[15:40] if num % 2 == 0]