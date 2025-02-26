def find_second_smallest_num(numbers):
    if not numbers or len(numbers) <= 41:
        return None
    subset = numbers[40:201]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]