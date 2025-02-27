def all_even_ints_exclusive(numbers):
    if len(numbers) > 9:
        return [num for num in numbers[8:9] if num % 2 == 0]
    else:
        return []