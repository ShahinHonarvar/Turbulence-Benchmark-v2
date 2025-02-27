def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[10:101])
    return sorted_numbers[9] if len(sorted_numbers) >= 10 else None