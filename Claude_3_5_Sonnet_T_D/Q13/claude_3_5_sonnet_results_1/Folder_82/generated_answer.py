def find_second_largest_num(numbers):
    if len(numbers) < 21:
        return None
    end_index = min(201, len(numbers))
    subset = numbers[20:end_index]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest