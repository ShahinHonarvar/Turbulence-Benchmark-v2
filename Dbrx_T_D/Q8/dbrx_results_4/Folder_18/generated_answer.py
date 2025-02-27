def all_even_ints_exclusive(numbers):
    start = 57
    end = 84
    if end - start < 0:
        return []
    return [num for num in numbers[start:end] if num % 2 == 0]