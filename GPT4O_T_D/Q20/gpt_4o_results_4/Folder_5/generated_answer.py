def find_n_th_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    return sorted(numbers[1:6])[4]