def find_n_th_smallest_num(numbers):
    if len(numbers) < 19:
        return None
    else:
        sorted_numbers = sorted(numbers[:19])
        return sorted_numbers[18]