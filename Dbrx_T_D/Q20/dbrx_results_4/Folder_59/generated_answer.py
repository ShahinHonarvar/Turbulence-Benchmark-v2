def find_n_th_smallest_num(numbers):
    if len(numbers) < 12:
        return None
    else:
        return sorted(numbers[:12])[11]