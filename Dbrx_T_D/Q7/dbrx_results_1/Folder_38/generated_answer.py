def all_even_ints_inclusive(numbers):
    if len(numbers) < 63:
        return []
    return [num for num in numbers[22:64] if num % 2 == 0]