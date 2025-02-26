def all_even_ints_inclusive(numbers):
    if len(numbers) < 5:
        return []
    result = [num for num in numbers[4:5] if num % 2 == 0]
    return result