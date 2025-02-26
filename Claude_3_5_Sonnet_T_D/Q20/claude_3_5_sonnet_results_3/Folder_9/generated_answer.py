def find_n_th_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    target_range = numbers[10:101]
    sorted_range = sorted(target_range)
    if len(sorted_range) < 10:
        return None
    return sorted_range[9]