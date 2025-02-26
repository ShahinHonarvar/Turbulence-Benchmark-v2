def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 5:
        return None
    subset = numbers[:5]
    subset.sort(reverse=True)
    return subset[1] if len(subset) >= 2 else None