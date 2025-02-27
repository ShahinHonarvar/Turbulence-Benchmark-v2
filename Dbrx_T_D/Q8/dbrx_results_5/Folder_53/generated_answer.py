def all_even_ints_exclusive(numbers):
    if len(numbers) < 102:
        return []
    else:
        return [num for num in numbers[100:102] if num % 2 == 0]