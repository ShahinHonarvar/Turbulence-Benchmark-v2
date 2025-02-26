def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 23:
        return None
    subset = numbers[22:89]
    if len(subset) < 2:
        return None
    try:
        smallest = min(subset)
        subset.remove(smallest)
        return min(subset)
    except ValueError:
        return None