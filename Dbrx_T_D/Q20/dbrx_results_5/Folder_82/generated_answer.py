def find_n_th_smallest_num(numbers):
    if not numbers or len(numbers) < 15:
        return None
    sorted_numbers = sorted(numbers[:15])
    return sorted_numbers[14]