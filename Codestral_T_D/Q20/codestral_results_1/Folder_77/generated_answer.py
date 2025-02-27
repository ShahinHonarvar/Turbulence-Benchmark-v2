def find_n_th_smallest_num(numbers):
    if len(numbers[106:255]) < 9:
        return None
    return sorted(numbers[106:255])[8]