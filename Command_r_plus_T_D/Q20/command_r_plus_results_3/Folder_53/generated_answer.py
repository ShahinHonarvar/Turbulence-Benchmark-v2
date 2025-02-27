def find_n_th_smallest_num(numbers_list: list[int]) -> int:
    nineteenth_smallest_num = sorted(numbers_list[18:190])[0]
    return nineteenth_smallest_num