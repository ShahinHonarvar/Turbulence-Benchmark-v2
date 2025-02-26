def find_second_largest_num(numbers):
    subset = numbers[6:9]
    if len(subset) < 2:
        return None
    return sorted(subset, reverse=True)[1]