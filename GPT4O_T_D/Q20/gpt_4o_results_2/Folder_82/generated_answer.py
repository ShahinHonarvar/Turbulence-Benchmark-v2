def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[:15])
    return sorted_numbers[14] if len(sorted_numbers) >= 15 else None