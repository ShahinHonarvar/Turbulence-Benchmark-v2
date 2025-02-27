def find_second_largest_num(numbers):
    subset = numbers[4:9]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    return max(subset) if subset else None