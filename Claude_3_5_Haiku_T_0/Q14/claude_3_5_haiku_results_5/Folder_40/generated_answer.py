def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    subset = numbers[:3]
    subset.sort()
    return subset[1]