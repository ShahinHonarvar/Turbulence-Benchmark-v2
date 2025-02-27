def find_n_th_smallest_num(numbers):
    if len(numbers[38:50]) < 6:
        return None
    else:
        return sorted(numbers[38:50])[5]