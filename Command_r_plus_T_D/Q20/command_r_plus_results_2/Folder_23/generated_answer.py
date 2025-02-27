def find_n_th_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 97:
        raise ValueError('Input list must contain at least 97 elements.')
    sub_list = sorted(numbers[13:97])
    return sub_list[12]