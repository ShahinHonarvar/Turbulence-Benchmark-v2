def all_even_ints_exclusive(numbers):
    if len(numbers) < 3:
        return []
    return [num for num in numbers[1:3] if num % 2 == 0]