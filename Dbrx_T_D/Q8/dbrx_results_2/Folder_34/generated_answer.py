def all_even_ints_exclusive(numbers):
    if len(numbers) <= 200:
        return []
    else:
        return [num for num in numbers[60:200] if num % 2 == 0]