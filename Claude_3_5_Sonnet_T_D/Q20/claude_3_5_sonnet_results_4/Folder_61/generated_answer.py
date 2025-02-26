def find_n_th_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    return sorted(numbers[:10])[9]