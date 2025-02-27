def all_even_ints_exclusive(numbers):
    if len(numbers) < 9:
        return []
    result = [n for n in numbers[7:9] if n % 2 == 0]
    return result