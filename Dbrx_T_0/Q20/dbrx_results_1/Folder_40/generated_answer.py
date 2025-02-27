def find_n_th_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        sorted_numbers = sorted(numbers[:5])
        return sorted_numbers[4]