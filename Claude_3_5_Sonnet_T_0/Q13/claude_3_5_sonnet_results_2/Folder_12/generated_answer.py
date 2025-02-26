def find_second_largest_num(numbers):
    if len(numbers) < 15:
        return None
    end_index = min(65, len(numbers))
    subset = numbers[14:end_index]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest