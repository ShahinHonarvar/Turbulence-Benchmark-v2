def find_n_th_smallest_num(numbers):
    if len(numbers) < 60 or len(numbers) < 35:
        return None
    return sorted(numbers[35:61])[3]