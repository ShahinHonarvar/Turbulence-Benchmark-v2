def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[30:301])
    return sorted_numbers[14] if len(sorted_numbers) > 14 else None