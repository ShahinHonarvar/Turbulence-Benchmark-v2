def all_even_ints_inclusive(numbers):
    if len(numbers) < 100:
        return []
    return [num for num in numbers[10:101] if num % 2 == 0]