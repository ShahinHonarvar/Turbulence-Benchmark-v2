def find_second_smallest_num(numbers):
    if len(numbers) <= 5:
        if len(numbers) < 2:
            return None
        return sorted(numbers)[1]
    subset = numbers[:6]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]