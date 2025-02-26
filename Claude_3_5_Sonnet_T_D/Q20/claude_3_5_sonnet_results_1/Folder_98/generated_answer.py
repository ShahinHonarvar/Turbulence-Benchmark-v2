def find_n_th_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    return sorted(numbers[:9])[8]