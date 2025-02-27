def find_n_th_smallest_num(numbers):
    if len(numbers) < 17:
        return None
    else:
        sorted_numbers = sorted(numbers)
        return sorted_numbers[16]