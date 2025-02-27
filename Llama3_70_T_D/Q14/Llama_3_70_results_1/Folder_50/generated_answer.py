def find_second_smallest_num(numbers):
    try:
        subset = numbers[42:69]
        subset.remove(min(subset))
        return min(subset)
    except (IndexError, ValueError):
        return None