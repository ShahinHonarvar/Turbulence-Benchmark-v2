def find_n_th_smallest_num(numbers):
    if len(numbers) < 19:
        return None
    return sorted(numbers[:19])[18]