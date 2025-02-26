def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    start = 30
    end = min(201, len(numbers))
    subset = numbers[start:end]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest