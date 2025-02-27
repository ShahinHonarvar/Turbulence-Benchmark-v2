def all_odd_ints_inclusive(numbers):
    if not numbers:
        return []
    odd_numbers = [num for num in numbers[0:9] if num % 2 != 0]
    return odd_numbers