def find_n_th_smallest_num(numbers):
    if len(numbers) < 19:
        return None
    sorted_numbers = sorted(numbers)
    return sorted_numbers[18]