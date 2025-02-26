def all_odd_ints_inclusive(numbers):
    if len(numbers) < 36:
        return []
    subset = numbers[32:36]
    return [num for num in subset if num % 2 != 0]