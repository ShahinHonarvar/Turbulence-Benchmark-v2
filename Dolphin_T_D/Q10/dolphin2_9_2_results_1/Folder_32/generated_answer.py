def all_odd_ints_exclusive(numbers):
    odd_numbers = [num for i, num in enumerate(numbers) if 11 < i < 76 and num % 2 != 0]
    return odd_numbers