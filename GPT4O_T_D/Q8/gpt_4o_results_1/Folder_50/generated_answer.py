def all_even_ints_exclusive(numbers):
    if len(numbers) <= 70:
        return []
    return [x for x in numbers[71:98] if x % 2 == 0]