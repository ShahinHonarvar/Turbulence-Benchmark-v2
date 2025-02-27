def find_n_th_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 191:
        raise ValueError('Input list must contain at least 191 elements.')
    return sorted(numbers[18:191])[18]