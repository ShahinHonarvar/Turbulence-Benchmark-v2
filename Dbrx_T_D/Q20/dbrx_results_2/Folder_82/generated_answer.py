def find_n_th_smallest_num(numbers):
    if len(numbers) < 15:
        return None
    else:
        sorted_numbers = sorted(numbers[:15])
        return sorted_numbers[14]