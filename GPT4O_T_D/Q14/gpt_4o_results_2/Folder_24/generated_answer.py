def find_second_smallest_num(numbers):
    if len(numbers) <= 23:
        return None
    sorted_subset = sorted(numbers[23:24])
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]