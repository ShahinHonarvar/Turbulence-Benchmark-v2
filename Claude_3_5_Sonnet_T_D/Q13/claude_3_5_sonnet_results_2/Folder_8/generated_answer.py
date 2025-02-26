def find_second_largest_num(numbers):
    if len(numbers) < 24 or len(numbers[23:24]) < 2:
        return None
    subset = numbers[23:24]
    largest = max(subset)
    second_largest = max((num for num in subset if num < largest))
    return second_largest