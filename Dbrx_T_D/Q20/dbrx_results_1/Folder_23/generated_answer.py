def find_n_th_smallest_num(numbers):
    if len(numbers) < 96:
        return None
    sorted_numbers = sorted(numbers[14:97])
    return sorted_numbers[12]