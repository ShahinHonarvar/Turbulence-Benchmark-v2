def find_n_th_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    else:
        first_six_numbers = numbers[:6]
        sorted_six_numbers = sorted(first_six_numbers)
        return sorted_six_numbers[5]