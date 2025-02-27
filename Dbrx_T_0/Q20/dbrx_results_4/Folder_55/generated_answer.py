def find_n_th_smallest_num(numbers):
    if len(numbers) < 13:
        return None
    else:
        sorted_numbers = sorted(numbers[:13])
        return sorted_numbers[12]