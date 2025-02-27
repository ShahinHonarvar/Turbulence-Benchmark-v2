def find_n_th_smallest_num(numbers):
    sorted_numbers = sorted(numbers[:18])
    return sorted_numbers[17] if len(sorted_numbers) >= 18 else None