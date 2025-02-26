def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[:8]) < 2:
        return None
    sorted_subset = sorted(numbers[:8])
    return sorted_subset[1]