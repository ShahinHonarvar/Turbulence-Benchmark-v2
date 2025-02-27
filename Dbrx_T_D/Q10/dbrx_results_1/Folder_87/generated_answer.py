def all_odd_ints_exclusive(numbers):
    if not numbers or len(numbers) < 99:
        return []
    odd_ints = [num for num in numbers[32:99] if num % 2 != 0]
    return odd_ints