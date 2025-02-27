def find_n_th_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    sorted_numbers = sorted(numbers[10:100])
    if len(sorted_numbers) < 10:
        return None
    return sorted_numbers[9]