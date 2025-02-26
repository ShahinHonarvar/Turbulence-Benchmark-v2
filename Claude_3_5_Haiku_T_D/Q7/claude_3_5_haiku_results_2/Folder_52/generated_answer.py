def all_even_ints_inclusive(numbers):
    if len(numbers) < 39:
        return []
    subset = numbers[28:39]
    return [num for num in subset if num % 2 == 0]