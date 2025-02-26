def find_second_largest_num(numbers):
    if len(numbers) < 2 or 200 >= len(numbers):
        return None
    subset = numbers[200:201]
    if len(subset) == 0:
        return None
    subset.sort(reverse=True)
    return subset[1] if len(subset) > 1 else None