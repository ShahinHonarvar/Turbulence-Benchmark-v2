def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[:4]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = max((n for n in subset if n != largest))
    return second_largest