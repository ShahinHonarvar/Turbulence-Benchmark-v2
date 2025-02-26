def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = numbers[:5]
    subset.sort()
    if len(subset) >= 2:
        return subset[1]
    else:
        return None