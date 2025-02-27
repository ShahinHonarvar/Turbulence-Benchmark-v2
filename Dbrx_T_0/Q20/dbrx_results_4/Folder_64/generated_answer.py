def find_n_th_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        sorted_numbers = sorted(numbers[:7])
        return sorted_numbers[6]