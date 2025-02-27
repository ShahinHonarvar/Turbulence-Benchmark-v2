def find_n_th_smallest_num(numbers):
    if len(numbers) < 16:
        return None
    sorted_numbers = sorted(numbers[:16])
    return sorted_numbers[15]