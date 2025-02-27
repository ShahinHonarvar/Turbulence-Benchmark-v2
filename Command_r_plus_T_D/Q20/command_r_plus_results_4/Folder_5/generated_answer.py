def find_n_th_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        raise ValueError('Input list must contain at least 5 numbers.')
    return sorted(numbers[1:6])[4]