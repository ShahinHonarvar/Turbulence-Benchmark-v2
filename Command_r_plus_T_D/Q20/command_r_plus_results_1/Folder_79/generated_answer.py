def find_n_th_smallest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        raise ValueError('Input list is empty.')
    sub_list = sorted(numbers_list[4:8])
    return sub_list[0]