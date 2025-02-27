def find_n_th_smallest_num(numbers):
    if len(numbers) < 16:
        return None
    return sorted(numbers[:16])[15]