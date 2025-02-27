def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 23:
        return None
    first_largest = max(numbers[:23])
    second_largest = max((num for num in numbers[:23] if num < first_largest))
    return second_largest