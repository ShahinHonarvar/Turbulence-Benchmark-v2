def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 24:
        return None
    subset = numbers[23:24]
    if len(subset) == 0:
        return None
    return subset[0]