def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[25:65])
    if len(sorted_numbers) >= 12:
        return sorted_numbers[11]
    else:
        return None