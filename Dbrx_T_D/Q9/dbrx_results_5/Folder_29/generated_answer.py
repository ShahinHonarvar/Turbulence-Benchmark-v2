def all_odd_ints_inclusive(numbers):
    if len(numbers) < 97:
        return []
    result = [num for num in numbers[59:98] if num % 2 != 0]
    return result