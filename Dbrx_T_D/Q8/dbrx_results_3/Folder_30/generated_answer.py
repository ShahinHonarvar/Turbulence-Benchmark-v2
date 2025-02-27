def all_even_ints_exclusive(numbers):
    if len(numbers) < 89:
        return []
    evens = [num for num in numbers[86:89] if num % 2 == 0]
    return evens