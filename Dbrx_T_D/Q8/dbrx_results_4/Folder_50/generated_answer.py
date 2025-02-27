def all_even_ints_exclusive(numbers):
    if len(numbers) < 98:
        return []
    return [num for num in numbers[70:98] if num % 2 == 0]