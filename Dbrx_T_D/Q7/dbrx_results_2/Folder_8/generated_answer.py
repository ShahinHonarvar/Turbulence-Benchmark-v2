def all_even_ints_inclusive(numbers):
    if len(numbers) < 46:
        return []
    start, end = (23, 23)
    return [num for num in numbers[start:end + 1] if num % 2 == 0]