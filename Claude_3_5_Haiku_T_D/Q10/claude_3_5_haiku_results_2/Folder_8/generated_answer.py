def all_odd_ints_exclusive(numbers):
    if len(numbers) <= 93:
        return []
    return [num for num in numbers[57:92] if num % 2 != 0]