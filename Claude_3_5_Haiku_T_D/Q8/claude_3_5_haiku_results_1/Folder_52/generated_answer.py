def all_even_ints_exclusive(numbers):
    if len(numbers) <= 95:
        return []
    result = [num for num in numbers[94:95] if num % 2 == 0]
    return result