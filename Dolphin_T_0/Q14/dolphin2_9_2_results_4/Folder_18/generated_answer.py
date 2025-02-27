def find_second_smallest_num(numbers):
    subset = numbers[30:48]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    subset.remove(smallest)
    if not subset:
        return None
    return min(subset)