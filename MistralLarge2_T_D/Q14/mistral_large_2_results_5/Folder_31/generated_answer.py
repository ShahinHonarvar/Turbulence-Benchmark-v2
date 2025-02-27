def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    subset = numbers[29:94]
    if len(subset) < 2:
        return None
    first_smallest = min(subset)
    subset.remove(first_smallest)
    second_smallest = min(subset)
    return second_smallest