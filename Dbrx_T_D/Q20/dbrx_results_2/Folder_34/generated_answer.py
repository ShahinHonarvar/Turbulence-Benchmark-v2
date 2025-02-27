def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[:19])
    return sorted_numbers[18] if len(numbers) >= 19 else min(sorted_numbers)