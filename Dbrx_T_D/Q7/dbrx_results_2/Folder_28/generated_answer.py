def all_even_ints_inclusive(numbers):
    start = 62
    end = 63
    if end < start or end >= len(numbers):
        return []
    return [num for num in numbers[start:end + 1] if num % 2 == 0]