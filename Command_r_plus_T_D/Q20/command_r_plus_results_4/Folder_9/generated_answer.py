def find_n_th_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError('Input list is empty.')
    sorted_numbers = sorted(numbers[10:101])
    return sorted_numbers[9]