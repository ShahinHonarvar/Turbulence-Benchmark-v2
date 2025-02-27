def find_n_th_smallest_num(numbers):
    if len(numbers) < 60 or len(numbers) < 100:
        return None
    sorted_numbers = sorted(numbers[39:100])
    if len(sorted_numbers) < 6:
        return None
    return sorted_numbers[5]