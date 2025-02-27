def find_n_th_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sorted_numbers = sorted(numbers[4:8])
    return sorted_numbers[3] if len(sorted_numbers) > 3 else None