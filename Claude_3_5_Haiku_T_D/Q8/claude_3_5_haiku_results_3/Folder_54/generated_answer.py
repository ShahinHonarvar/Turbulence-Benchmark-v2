def all_even_ints_exclusive(numbers):
    if len(numbers) <= 35:
        return []
    subset = numbers[28:34]
    return [num for num in subset if num % 2 == 0]