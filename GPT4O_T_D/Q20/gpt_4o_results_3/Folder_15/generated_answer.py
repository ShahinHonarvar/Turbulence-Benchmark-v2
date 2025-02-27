def find_n_th_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    sorted_numbers = sorted(numbers[:6])
    return sorted_numbers[5]