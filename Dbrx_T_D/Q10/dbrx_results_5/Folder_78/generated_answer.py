def all_odd_ints_exclusive(numbers):
    if len(numbers) < 36:
        return []
    odd_ints = [num for num in numbers[20:35] if num % 2 != 0]
    return odd_ints