def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 63 - 22 + 1:
        return None
    first_largest = max(numbers[22:63])
    numbers_without_first_largest = [num for num in numbers if num != first_largest]
    if len(numbers_without_first_largest) < 1 or len(numbers_without_first_largest) < 63 - 22:
        return None
    second_largest = max(numbers_without_first_largest[22:63])
    return second_largest