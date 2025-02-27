def find_n_th_smallest_num(numbers):
    if len(numbers) < 85 or len(numbers) < 69:
        return None
    return sorted(numbers[68:86])[6]