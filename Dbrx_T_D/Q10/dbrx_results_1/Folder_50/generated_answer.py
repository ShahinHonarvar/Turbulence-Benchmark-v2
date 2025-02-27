def all_odd_ints_exclusive(numbers):
    if len(numbers) < 98:
        return []
    odd_ints = [num for num in numbers[69:98] if num % 2 != 0]
    return odd_ints