def find_second_largest_num(numbers):
    if len(numbers) < 22 or len(numbers) <= 200:
        return None
    subset = numbers[20:201]
    subset.sort(reverse=True)
    return subset[1] if len(subset) > 1 else None