def all_even_ints_exclusive(numbers):
    if len(numbers) < 99:
        return []
    result = [num for num in numbers[86:99] if num % 2 == 0]
    return result