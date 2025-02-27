def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[10:91])
    if 13 > len(sorted_numbers) + 10:
        return None
    else:
        return sorted_numbers[13]