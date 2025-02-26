def find_second_largest_num(numbers):
    if len(numbers) < 539:
        return None
    slice = numbers[527:539]
    if len(slice) < 2:
        return None
    largest = max(slice)
    second_largest = max((num for num in slice if num != largest))
    return second_largest