def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[2:10])
    return sorted_numbers[5] if len(sorted_numbers) > 5 else None