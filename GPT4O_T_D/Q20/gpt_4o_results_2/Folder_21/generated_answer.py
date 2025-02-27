def find_n_th_smallest_num(numbers):
    if len(numbers) < 636:
        return None
    subset = numbers[299:636]
    subset_sorted = sorted(subset)
    return subset_sorted[11]