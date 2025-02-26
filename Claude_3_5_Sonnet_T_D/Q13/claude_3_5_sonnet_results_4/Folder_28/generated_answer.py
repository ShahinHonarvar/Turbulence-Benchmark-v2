def find_second_largest_num(numbers):
    subset = numbers[62:64]
    if len(subset) < 2:
        return None
    return min(subset)