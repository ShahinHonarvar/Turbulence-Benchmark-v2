def find_second_largest_num(numbers):
    if len(numbers) < 210:
        return None
    end_index = min(556, len(numbers) - 1)
    subset = numbers[209:end_index + 1]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest if second_largest != largest else None