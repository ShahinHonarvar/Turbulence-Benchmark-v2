def find_n_th_smallest_num(numbers):
    if len(numbers) < 14:
        return None
    else:
        sorted_numbers = sorted(numbers)
        return sorted_numbers[13]