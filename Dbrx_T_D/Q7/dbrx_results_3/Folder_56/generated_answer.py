def all_even_ints_inclusive(numbers):
    if not numbers:
        return []
    return [num for num in numbers[:1] if num % 2 == 0]