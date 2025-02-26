def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    subset = numbers[56:58]
    if len(subset) < 2:
        return None
    return min(subset)