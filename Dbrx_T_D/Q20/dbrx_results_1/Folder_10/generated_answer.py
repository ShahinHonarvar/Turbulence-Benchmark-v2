def find_n_th_smallest_num(numbers):
    if len(numbers) < 96 or len(numbers) < 56:
        return None
    sorted_numbers = sorted(numbers[56:97])
    if len(sorted_numbers) >= 18:
        return sorted_numbers[17]
    else:
        return None