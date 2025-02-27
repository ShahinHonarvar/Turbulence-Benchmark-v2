def all_odd_ints_inclusive(numbers):
    if len(numbers) < 39:
        return []
    odd_ints = [num for num in numbers[27:39] if num % 2 != 0]
    return odd_ints