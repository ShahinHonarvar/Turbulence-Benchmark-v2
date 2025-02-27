def find_n_th_smallest_num(numbers):
    if len(numbers) < 88:
        raise ValueError('Input list should have at least 88 elements')
    relevant_numbers = sorted(numbers[54:88])
    return relevant_numbers[12]