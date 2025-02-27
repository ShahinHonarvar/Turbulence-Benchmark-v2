def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[10:91])
    if len(sorted_numbers) >= 13:
        return sorted_numbers[12]
    else:
        return None