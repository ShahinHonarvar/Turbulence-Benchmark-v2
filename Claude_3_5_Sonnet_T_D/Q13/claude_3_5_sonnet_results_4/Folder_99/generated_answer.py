def find_second_largest_num(numbers):
    subset = numbers[310:371]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = max((num for num in subset if num != largest))
    return second_largest if second_largest != largest else None