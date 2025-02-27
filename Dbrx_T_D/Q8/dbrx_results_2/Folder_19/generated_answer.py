def all_even_ints_exclusive(numbers):
    if len(numbers) < 5:
        return []
    else:
        return [num for num in numbers[2:5] if num % 2 == 0]