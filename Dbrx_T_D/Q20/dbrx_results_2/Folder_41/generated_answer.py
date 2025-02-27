def find_n_th_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sorted_numbers = sorted(numbers[4:9])
    return sorted_numbers[3]