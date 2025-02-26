def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    subset = numbers[:3]
    subset.sort(reverse=True)
    return subset[1] if len(subset) >= 2 else None