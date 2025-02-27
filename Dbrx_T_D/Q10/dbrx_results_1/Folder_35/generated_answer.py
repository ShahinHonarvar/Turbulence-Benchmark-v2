def all_odd_ints_exclusive(numbers):
    if len(numbers) < 80:
        return []
    odd_ints = [num for num in numbers[10:79] if num % 2 != 0]
    return odd_ints