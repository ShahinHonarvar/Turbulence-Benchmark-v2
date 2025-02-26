def find_n_th_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    return sorted(numbers[:8])[7]