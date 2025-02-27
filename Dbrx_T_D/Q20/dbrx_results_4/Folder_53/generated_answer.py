def find_n_th_smallest_num(numbers):
    if len(numbers) < 190 or len(numbers) > 1000:
        return None
    return sorted(numbers[19:191])[18]