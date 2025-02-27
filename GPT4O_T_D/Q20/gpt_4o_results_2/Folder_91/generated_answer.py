def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[:8])
    return sorted_numbers[7] if len(sorted_numbers) >= 8 else None