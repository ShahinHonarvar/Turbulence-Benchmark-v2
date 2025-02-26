def all_odd_ints_exclusive(numbers):
    if len(numbers) <= 93:
        return []
    subset = numbers[79:93]
    return [num for num in subset if num % 2 != 0]