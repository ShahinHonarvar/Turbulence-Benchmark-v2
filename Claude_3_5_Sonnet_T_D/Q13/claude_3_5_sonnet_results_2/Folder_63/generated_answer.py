def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    subset = numbers[22:89]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest