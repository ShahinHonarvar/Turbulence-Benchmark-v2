def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[260:823])
    return sorted_numbers[9] if len(sorted_numbers) > 9 else None