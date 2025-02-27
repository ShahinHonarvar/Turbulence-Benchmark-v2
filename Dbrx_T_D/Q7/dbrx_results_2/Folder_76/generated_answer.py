def all_even_ints_inclusive(numbers):
    if len(numbers) < 987:
        return []
    start, end = (686, 987)
    return [num for num in numbers[start:end + 1] if num % 2 == 0]