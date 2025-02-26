def find_second_largest_num(numbers):
    if len(numbers) <= 1 or len(numbers) < 11:
        return None
    subset = numbers[:11]
    subset.sort(reverse=True)
    return subset[1] if len(subset) >= 2 else None