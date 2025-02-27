def find_n_th_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError('Input list is empty.')
    if len(numbers) < 92:
        raise ValueError('Input list must have at least 92 elements.')
    sorted_numbers = sorted(numbers[10:92])
    return sorted_numbers[12]