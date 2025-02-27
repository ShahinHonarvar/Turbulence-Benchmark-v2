def find_n_th_smallest_num(numbers):
    relevant_numbers = numbers[299:636]
    relevant_numbers.sort()
    return relevant_numbers[11]