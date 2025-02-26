def find_second_largest_num(numbers):
    if len(numbers) <= 41:
        return None
    subset = numbers[40:201]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest