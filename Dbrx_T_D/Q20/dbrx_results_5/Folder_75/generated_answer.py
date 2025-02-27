def find_n_th_smallest_num(numbers):
    if len(numbers) < 82:
        return None
    return sorted(numbers[18:83])[5]