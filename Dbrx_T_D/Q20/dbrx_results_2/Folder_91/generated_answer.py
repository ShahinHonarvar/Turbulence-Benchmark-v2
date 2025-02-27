def find_n_th_smallest_num(numbers):
    if not numbers or len(numbers) < 8:
        return None
    numbers = sorted(numbers[:8])
    return numbers[7]