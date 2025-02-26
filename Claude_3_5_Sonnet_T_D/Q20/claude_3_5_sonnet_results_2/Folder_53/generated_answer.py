def find_n_th_smallest_num(numbers):
    if len(numbers) < 191:
        return None
    subset = numbers[19:191]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 19:
        return None
    return sorted_subset[18]