def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    subset = numbers[1:9]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]