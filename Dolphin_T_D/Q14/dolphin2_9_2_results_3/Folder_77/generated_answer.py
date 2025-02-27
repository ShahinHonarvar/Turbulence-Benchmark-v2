def find_second_smallest_num(numbers):
    if len(numbers) < 976:
        return None
    subset = numbers[639:976]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    subset.remove(smallest)
    if len(subset) == 0:
        return None
    return min(subset)