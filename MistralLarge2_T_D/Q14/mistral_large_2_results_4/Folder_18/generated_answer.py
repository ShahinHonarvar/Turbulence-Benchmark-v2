def find_second_smallest_num(numbers):
    subset = numbers[30:49]
    if len(subset) < 2:
        return None
    first_smallest = min(subset)
    subset.remove(first_smallest)
    second_smallest = min(subset)
    return second_smallest