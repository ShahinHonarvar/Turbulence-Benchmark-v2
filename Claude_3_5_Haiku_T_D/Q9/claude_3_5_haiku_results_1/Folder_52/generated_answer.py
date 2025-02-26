def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 38:
        return []
    odd_numbers = [num for num in numbers[28:39] if num % 2 != 0]
    return odd_numbers