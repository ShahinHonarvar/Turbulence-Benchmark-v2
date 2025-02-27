def find_n_th_smallest_num(numbers):
    subset = sorted(numbers[15:25])
    return subset[6] if len(subset) >= 7 else None