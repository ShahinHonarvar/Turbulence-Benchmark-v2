def all_odd_ints_exclusive(numbers):
    if len(numbers) < 84:
        return []
    odd_ints = [num for num in numbers[73:84] if num % 2 != 0]
    return odd_ints