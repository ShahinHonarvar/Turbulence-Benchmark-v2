def find_n_th_smallest_num(numbers):
    if len(numbers) < 191:
        return None
    subset = sorted(numbers[19:191])
    return subset[18]