def find_n_th_smallest_num(numbers):
    if len(numbers) < 98 or len(numbers) > 1000:
        return None
    sorted_numbers = sorted(numbers[29:99])
    return sorted_numbers[4]