def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    subset = numbers[8:10]
    if len(subset) < 2:
        return None
    return sorted(subset, reverse=True)[1]