def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[:9])
    return sorted_numbers[8] if len(numbers) >= 9 else min(sorted_numbers)