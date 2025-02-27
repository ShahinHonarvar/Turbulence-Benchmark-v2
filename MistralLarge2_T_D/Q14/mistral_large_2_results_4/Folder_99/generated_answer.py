def find_second_smallest_num(numbers):
    subset = numbers[608:610]
    if len(subset) >= 2:
        return sorted(subset)[1]
    return None