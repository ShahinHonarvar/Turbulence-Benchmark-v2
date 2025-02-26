def find_n_th_smallest_num(numbers):
    subset = numbers[54:88]
    sorted_subset = sorted(subset)
    return sorted_subset[12] if len(sorted_subset) >= 13 else None