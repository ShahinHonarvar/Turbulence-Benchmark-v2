def find_n_th_smallest_num(numbers):
    return sorted(numbers[:12])[11] if len(numbers) >= 12 else None