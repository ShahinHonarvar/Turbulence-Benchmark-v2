def find_n_th_smallest_num(numbers):
    sliced_numbers = numbers[34:95]
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[17] if len(sorted_numbers) >= 18 else None