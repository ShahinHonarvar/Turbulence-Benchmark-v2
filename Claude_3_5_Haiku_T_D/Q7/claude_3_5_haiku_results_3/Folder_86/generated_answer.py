def all_even_ints_inclusive(numbers):
    if len(numbers) < 35:
        return []
    subset = numbers[31:35]
    return [num for num in subset if num % 2 == 0]