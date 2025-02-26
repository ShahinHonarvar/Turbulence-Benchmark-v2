def all_odd_ints_inclusive(numbers):
    if len(numbers) < 7:
        return []
    odd_numbers = [num for num in numbers[6:7] if num % 2 != 0]
    return odd_numbers