def all_even_ints_inclusive(numbers):
    if 73 < len(numbers):
        return [num for num in numbers[73:74] if num % 2 == 0]
    return []