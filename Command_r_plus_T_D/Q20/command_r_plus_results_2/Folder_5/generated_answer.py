def find_n_th_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        raise ValueError('Input list must contain at least 5 elements.')
    sorted_numbers = sorted(numbers[1:5])
    return sorted_numbers[4]