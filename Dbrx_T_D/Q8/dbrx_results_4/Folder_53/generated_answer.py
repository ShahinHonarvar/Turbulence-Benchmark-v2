def all_even_ints_exclusive(numbers):
    if len(numbers) < 102:
        return []
    return [num for num in numbers[100:101] if num % 2 == 0]