def find_n_th_smallest_num(numbers):
    if len(numbers) < 49 or len(numbers) > 100:
        return None
    sorted_numbers = sorted(numbers[38:50])
    if len(sorted_numbers) < 6:
        return None
    return sorted_numbers[5]