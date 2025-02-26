def find_n_th_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    return sorted(numbers[:4])[3]