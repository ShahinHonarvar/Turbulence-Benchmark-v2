def find_n_th_smallest_num(numbers):
    if len(numbers) < 18:
        return None
    else:
        sorted_numbers = sorted(numbers[:18])
        return sorted_numbers[17]