def find_second_smallest_num(numbers):
    if len(numbers) < 67 or len(numbers[64:67]) < 2:
        return None
    subset = numbers[64:67]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 2:
        return sorted_subset[1]
    else:
        return None