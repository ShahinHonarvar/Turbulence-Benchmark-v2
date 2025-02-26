def all_odd_ints_exclusive(numbers):
    if len(numbers) <= 49:
        return []
    subset = numbers[29:49]
    return [num for num in subset if num % 2 != 0]