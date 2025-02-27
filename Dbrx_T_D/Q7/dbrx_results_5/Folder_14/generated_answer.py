def all_even_ints_inclusive(numbers):
    if len(numbers) >= 8:
        return [num for num in numbers[5:8] if num % 2 == 0]
    else:
        return []