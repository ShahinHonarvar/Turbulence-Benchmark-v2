def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[47:90])
    return sorted_numbers[6] if len(sorted_numbers) >= 7 else None