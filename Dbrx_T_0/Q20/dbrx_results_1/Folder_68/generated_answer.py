def find_n_th_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    return sorted(numbers[:11])[10]