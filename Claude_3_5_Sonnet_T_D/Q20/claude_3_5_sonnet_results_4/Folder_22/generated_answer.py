def find_n_th_smallest_num(numbers):
    if len(numbers) < 17:
        return None
    return sorted(numbers[:17])[16]