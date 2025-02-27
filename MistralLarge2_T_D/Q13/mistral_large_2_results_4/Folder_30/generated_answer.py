def find_second_largest_num(numbers):
    if len(numbers) < 99:
        return None
    subset = numbers[55:99]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest