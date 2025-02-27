def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[:14])
    return sorted_numbers[13] if len(sorted_numbers) > 13 else None