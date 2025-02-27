def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[:16])
    return sorted_numbers[15] if len(sorted_numbers) >= 16 else None