def find_second_largest_num(numbers):
    subset = numbers[22:89]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    if len(subset) < 2:
        return None
    second_largest = max(subset)
    return second_largest