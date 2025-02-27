def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[14] if len(numbers) >= 15 else None