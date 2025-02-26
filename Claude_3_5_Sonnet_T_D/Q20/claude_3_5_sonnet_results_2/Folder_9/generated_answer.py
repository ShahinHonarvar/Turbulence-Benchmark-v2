def find_n_th_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    relevant_numbers = numbers[10:101]
    sorted_numbers = sorted(relevant_numbers)
    if len(sorted_numbers) < 10:
        return None
    return sorted_numbers[9]