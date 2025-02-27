def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 63 - 22 + 1:
        return None
    first_largest = max(numbers[22:63])
    numbers = [n for n in numbers[22:63] if n < first_largest]
    if not numbers:
        return None
    return max(numbers)