def all_odd_ints_inclusive(numbers):
    if len(numbers) < 36:
        return []
    odd_ints = [num for num in numbers[32:36] if num % 2 != 0]
    return odd_ints