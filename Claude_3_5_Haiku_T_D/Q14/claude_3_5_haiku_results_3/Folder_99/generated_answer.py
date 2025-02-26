def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 610:
        return None
    subset = numbers[608:610]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]